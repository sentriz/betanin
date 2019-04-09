# 3rd party
from flask_restplus import abort
from flask_jwt_extended import jwt_required

# betanin
from betanin import main_config
from betanin.jobs import import_torrents
from betanin.rest.base import BaseResource
from betanin.rest.base import SecureResource
from betanin.extensions import db
from betanin.rest.models import request as req_models
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import torrents_ns
from betanin.orm.models.torrent import Torrent


@torrents_ns.route("/")
class TorrentsResource(SecureResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.torrents)
    @torrents_ns.marshal_list_with(resp_models.torrent)
    def get():
        "gets the list of all torrents"
        args = req_models.torrents.parse_args()
        torrents = Torrent.query.order_by(Torrent.updated.desc())
        if args["page"] and args["per_page"]:
            page = torrents.paginate(**args, error_out=False)
            return page.items
        return torrents.all()


# not based on SecureResource because the POST called by the torrent clients
# (which use the api key for auth), and the PUT and DELETE is made by the frontend,
# (which use a json web token for auth). For those there is the @jwt_required -
# which is usually implied by the SecureResource
@torrents_ns.route("/<string:torrent_id>")
class TorrentResource(BaseResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.torrent)
    @torrents_ns.doc(security=None)
    @torrents_ns.response(422, "invalid api key")
    def post(torrent_id):
        "imports a new torrent"
        args = req_models.torrent.parse_args()
        if not main_config.api_key_correct(args["X-API-Key"]):
            abort(422, "invalid api key")
            return
        import_torrents.add(
            id=torrent_id, name=args["name"], path=args["path"]
        )

    @staticmethod
    @jwt_required
    def put(torrent_id):
        "trys to import a torrent again"
        import_torrents.retry(torrent_id)

    @staticmethod
    @jwt_required
    def delete(torrent_id):
        "deletes a torrent from the list"
        query = Torrent.query.filter_by(id=torrent_id)
        torrent = query.first_or_404()
        db.session.delete(torrent)
        db.session.commit()


@torrents_ns.route("/<string:torrent_id>/console/stdout")
class StdoutResource(SecureResource):
    @staticmethod
    @torrents_ns.marshal_list_with(resp_models.line)
    def get(torrent_id):
        "gets the stdout of an imported/importing torrent"
        matches = Torrent.query.filter_by(id=torrent_id)
        return matches.first_or_404().lines


@torrents_ns.route("/<string:torrent_id>/console/stdin")
class StdinResource(SecureResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.line)
    def post(torrent_id):
        "sends stdin to an importing torrent"
        args = req_models.line.parse_args()
        text = args["text"]
        import_torrents.send_input(torrent_id, text)
