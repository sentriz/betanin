from flask import request
from flask import abort

from betanin.api.orm.models.torrent import Torrent
from betanin.api.rest.models import response as response_models
from betanin.api.rest.models import request as request_models
from betanin.api.rest.base import BaseResource
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.jobs.process_torrents import PROCESSES


@torrents_ns.route('/')
class TorrentsResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_list_with(response_models.torrent)
    def get():
        return Torrent.query.all()


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
        if torrent_id not in PROCESSES:
            abort(404)
        content = request.get_json(silent=True)
        PROCESSES[torrent_id].communicate(
            input=content['text']
        )
