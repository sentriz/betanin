from app.api import api_rest
from app.api.rest.base import BaseResource
from app.api import torrent_client


@api_rest.route('/transmission')
class TorrentsResource(BaseResource):
    def get(self):
        # return list(torrent_client.get_torrents())
        return [], 204
