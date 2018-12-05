# 3rd party
from flask import request

# betanin
from betanin.api import events
from betanin.api.jobs import import_torrents
from betanin.extensions import db
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as request_models
from betanin.api.rest.models import response as response_models
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.orm.models.torrent import Torrent


@torrents_ns.route('/')
class TorrentsResource(BaseResource):
    @staticmethod
    @torrents_ns.marshal_list_with(response_models.torrent)
    def get():
        return Torrent.query \
            .order_by(Torrent.created.desc()) \
            .all()


@torrents_ns.route('/<string:torrent_id>')
class TorrentResource(BaseResource):
    @staticmethod
    @torrents_ns.expect(request_models.torrent)
    def post(torrent_id):
        content = request.form
        import_torrents.add(
            id=torrent_id,
            path=content['path'],
            name=content['name'],
        )

    @staticmethod
    def put(torrent_id):
        import_torrents.retry(torrent_id)


    @staticmethod
    def delete(torrent_id):
        query = Torrent.query.filter_by(id=torrent_id)
        torrent = query.first_or_404()
        torrent.delete_lines()
        query.delete()
        db.session.commit()
        events.torrents_changed()


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
        content = request.get_json(silent=True)
        text = content['text'].encode()
        import_torrents.send_input(torrent_id, text)
