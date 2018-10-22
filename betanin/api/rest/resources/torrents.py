from flask import request
from flask import abort

from betanin.api.orm.models.torrent import Torrent
from betanin.api.jobs.import_torrents import PROCESSES
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as request_models
from betanin.api.rest.models import response as response_models
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.status import BetaStatus
from betanin.api.status import global_status


@torrents_ns.route('/')
class TorrentsResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_with(response_models.fetch)
    def get():
        return {
            'torrents': Torrent.query \
                .filter(Torrent.beta_status != BetaStatus.IGNORED),
                # .filter(Torrent.beta_status != BetaStatus.UNKNOWN)
            'status': global_status,
        }


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
