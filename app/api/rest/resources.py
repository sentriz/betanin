from datetime import datetime

from app.api import api_rest
from app.api.paths import config
from app.api.rest.base import BaseResource, SecureResource
from app.api import torrent_client
from flask import request
from flask_restplus import Api


@api_rest.route('/transmission')
class TransmissionResource(BaseResource):
    def get(self):
        return list(torrent_client.get_torrents())
