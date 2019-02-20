# betanin
from betanin.api import events
from betanin.api.jobs import import_torrents
from betanin.extensions import db
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as req_models
from betanin.api.rest.models import response as resp_models
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.orm.models.torrent import Torrent


@torrents_ns.route('/')
class TorrentsResource(BaseResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.torrents)
    @torrents_ns.marshal_list_with(resp_models.torrent)
    def get():
        'gets the list of all torrents'
        args = req_models.torrents.parse_args()
        torrents = Torrent.query.order_by(
            Torrent.updated.desc())
        if args['page'] and args['per_page']:
            page = torrents.paginate(**args, error_out=False)
            return page.items
        return torrents.all()


@torrents_ns.route('/<string:torrent_id>')
class TorrentResource(BaseResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.torrent)
    def post(torrent_id):
        'imports a new torrent'
        args = req_models.torrent.parse_args()
        import_torrents.add(
            id=torrent_id,
            name=args['name'],
            path=args['path'],
        )

    @staticmethod
    def put(torrent_id):
        'trys to import a torrent again'
        import_torrents.retry(torrent_id)

    @staticmethod
    def delete(torrent_id):
        'deletes a torrent from the list'
        query = Torrent.query.filter_by(id=torrent_id)
        torrent = query.first_or_404()
        db.session.delete(torrent)
        db.session.commit()


@torrents_ns.route('/<string:torrent_id>/console/stdout')
class StdoutResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_list_with(resp_models.line)
    def get(torrent_id):
        'gets the stdout of an imported/importing torrent'
        matches = Torrent.query.filter_by(id=torrent_id)
        return matches.first_or_404().lines


@torrents_ns.route('/<string:torrent_id>/console/stdin')
class StdinResource(BaseResource):
    @staticmethod
    @torrents_ns.doc(parser=req_models.line)
    def post(torrent_id):
        'sends stdin to an importing torrent'
        args = req_models.line.parse_args()
        text = args['text'].encode()
        import_torrents.send_input(torrent_id, text)
