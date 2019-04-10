# 3rd party
from flask_restplus import abort
from flask_jwt_extended import jwt_required

# betanin
from betanin import main_config
from betanin.jobs import import_torrents
from betanin.rest.base import BaseResource
from betanin.rest.base import SecureResource
from betanin.extensions import DB
from betanin.rest.models import request as req_models
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import TORRENTS_NS
from betanin.orm.models.torrent import Torrent


@TORRENTS_NS.route("/")
class TorrentsResource(SecureResource):
    @staticmethod
    @TORRENTS_NS.doc(parser=req_models.TORRENTS)
    @TORRENTS_NS.marshal_list_with(resp_models.TORRENT)
    def get():
        "gets the list of all torrents"
        args = req_models.TORRENTS.parse_args()
        torrents = Torrent.query.order_by(Torrent.updated.desc())
        if args["page"] and args["per_page"]:
            page = torrents.paginate(**args, error_out=False)
            return page.items
        return torrents.all()


# not based on SecureResource because the POST called by the torrent clients
# (which use the api key for auth), and the PUT and DELETE is made by the
# frontend, (which use a json web token for auth). For those there is
# the @jwt_required - which is usually implied by the SecureResource
@TORRENTS_NS.route("/<string:torrent_id>")
class TorrentResource(BaseResource):
    @staticmethod
    @TORRENTS_NS.doc(parser=req_models.TORRENT)
    @TORRENTS_NS.doc(security=None)
    @TORRENTS_NS.response(422, "invalid api key")
    def post(torrent_id):
        "imports a new torrent"
        args = req_models.TORRENT.parse_args()
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
        DB.session.delete(torrent)
        DB.session.commit()


@TORRENTS_NS.route("/<string:torrent_id>/console/stdout")
class StdoutResource(SecureResource):
    @staticmethod
    @TORRENTS_NS.marshal_list_with(resp_models.LINE)
    def get(torrent_id):
        "gets the stdout of an imported/importing torrent"
        matches = Torrent.query.filter_by(id=torrent_id)
        return matches.first_or_404().lines


@TORRENTS_NS.route("/<string:torrent_id>/console/stdin")
class StdinResource(SecureResource):
    @staticmethod
    @TORRENTS_NS.doc(parser=req_models.LINE)
    def post(torrent_id):
        "sends stdin to an importing torrent"
        args = req_models.LINE.parse_args()
        text = args["text"]
        import_torrents.send_input(torrent_id, text)
