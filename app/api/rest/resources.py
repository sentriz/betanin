from app import api
from app.api import api_rest
from app.api import torrent_client
from app.api.rest import response_models
from app.api.rest.base import BaseResource
from app.api.rest.namespaces import torrents_ns


@torrents_ns.route('/all')
class TorrentsResource(BaseResource):
    @torrents_ns.marshal_list_with(response_models.torrent)
    def get(self):
        return api.torrents