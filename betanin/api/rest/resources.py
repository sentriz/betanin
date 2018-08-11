from betanin import api
from betanin.api import api_rest
from betanin.api import torrent_client
from betanin.api.rest import response_models
from betanin.api.rest.base import BaseResource
from betanin.api.rest.namespaces import torrents_ns


@torrents_ns.route('/all')
class TorrentsResource(BaseResource):
    @torrents_ns.marshal_list_with(response_models.torrent)
    def get(self):
        return api.torrents
