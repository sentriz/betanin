from betanin.api.rest.models import response as response_models
from betanin.api.rest.models import request as request_models
from betanin.api.rest.base import BaseResource
from betanin.api.rest.namespaces import settings_ns
from betanin.api import torrent_client


@settings_ns.route('/remotes')
class RemotesResources(BaseResource):
    @staticmethod
    def get():
        'list the supported remotes'
        return torrent_client.get_remote_names()


@settings_ns.route('/remotes/<string:remote>')
class RemotesResources(BaseResource):
    @staticmethod
    def get(remote):
        'gets the fields for a remote'
        fields = torrent_client.get_fields(remote)
        if not fields:
            abort(404)
        return fields

    def put(remote):
        'configure the remote'
