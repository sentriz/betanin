# 3rd party
from flask import abort
from flask import request

# betanin
from betanin import beets
from betanin.api.rest.base import BaseResource
from betanin.api.rest.namespaces import settings_ns


@settings_ns.route('/beets/config')
class TorrentResource(BaseResource):
    @staticmethod
    def get():
        config = beets.get_config()
        if not config:
            return abort(400, 'config does not exist')
        return config


    @staticmethod
    def put():
        content = request.get_data()
        beets.set_config(content)
