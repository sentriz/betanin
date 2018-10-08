from betanin.api import torrent_client
from betanin.api.orm.models.remote import Remote
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as request_models
from betanin.api.rest.models import response as response_models
from betanin.api.rest.namespaces import settings_ns
from betanin.extensions import db


@settings_ns.route('/remotes')
class RemotesResources(BaseResource):
    @staticmethod
    @settings_ns.marshal_list_with(response_models.remote)
    def get():
        'get all remote configs'
        return Remote.query.all()


@settings_ns.route('/remotes/configure/<int:remote_id>')
class RemotesResources(BaseResource):
    @staticmethod
    def put(remote_id):
        'update a remotes config'
        remote = Remote.query.filter_by(id=remote_id).first_or_404()
        remote.config = request.get_json(silent=True)
        db.session.commit()


@settings_ns.route('/remotes/add/<string:remote_type>')
class RemotesResources(BaseResource):
    @staticmethod
    @settings_ns.marshal_with(response_models.remote)
    def put(remote_type):
        'creates a new remote'
        empty_config = torrent_client.get_default_config(remote_type)
        remote = Remote(type=remote_type,
                        config=empty_config)
        db.session.add(remote)
        db.session.commit()
        return remote
