# 3rd party
from flask import abort
from flask import request

# betanin
from betanin.api import status
from betanin.api.jobs import import_torrents
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as request_models
from betanin.api.rest.models import response as response_models
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.orm.models.torrent import Torrent


@torrents_ns.route('/')
class TorrentsResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_with(response_models.fetch)
    def get():
        return {
            'torrents': Torrent.query.order_by(Torrent.created.desc()).all(),
            'status': status.fetch(),
        }

    @staticmethod
    @torrents_ns.expect(request_models.torrent)
    def post():
        content = request.form
        import_torrents.add(
            id=content['id'],
            path=content['path'],
            name=content['name'],
        )

    @staticmethod
    @torrents_ns.expect(request_models.torrent)
    def delete():
        content = request.form
        import_torrents.remove(
            id=content['id'],
            path=content['path'],
            name=content['name']
        )

@torrents_ns.route('/<string:torrent_id>/console/stdout')
class StdoutResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_list_with(response_models.line)
    def get(torrent_id):
        matches = Torrent.query.filter_by(id=torrent_id)
        return matches.first_or_404().lines


@torrents_ns.route('/<string:torrent_id>/console/stdin')
class StdinResource(BaseResource):
    @staticmethod
    @torrents_ns.expect(request_models.line)
    def post(torrent_id):
        if torrent_id not in import_torrents.PROCESSES:
            abort(404)
        content = request.get_json(silent=True)
        import_torrents.PROCESSES[torrent_id].communicate(
            input=content['text']
        )
