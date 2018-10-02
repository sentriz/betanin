from betanin.api.rest.models import response as response_models
from betanin.api.rest.models import request as request_models
from betanin.api.rest.base import BaseResource
from betanin.api.rest.namespaces import settings_ns
from betanin.api import torrent_client


@settings_ns.route('/remotes/config')
class RemotesResources(BaseResource):
    @staticmethod
    @settings_ns.marshal_list_with(response_models.remote)
    def get(remote):
        'get all remote configs'
        return Remote.query.all()


@settings_ns.route('/remotes/config/<int:remote_id>')
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
    def put(remote_type):
        'creates a new remote'
        db.session.add(Remote(type=remote_type))
