# 3rd party
from flask import abort
from flask import request

# betanin
from betanin import beets
from betanin.api import notifications
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


@settings_ns.route('/notifications/services')
class NotificationsResource(BaseResource):
    @staticmethod
    def get():
        'gets all services'
        return notifications.get_services()

    @staticmethod
    def post():
        'creates template for new service'
        content = request.get_json()
        type_ = content['type']
        return notifications.add_service(type_)


@settings_ns.route('/notifications/services/<string:service_id>')
class NotificationResource(BaseResource):
    @staticmethod
    def put(service_id):
        'updates a service'
        service = request.get_json()
        print(service, 'HELLOs')
        notifications.update_service(service_id, service)

    @staticmethod
    def delete(service_id):
        'deletes a service'
        return notifications.remove_service(service_id)


@settings_ns.route('/notifications/possible_services')
class TorrentResource(BaseResource):
    @staticmethod
    def get():
        return notifications.get_possible_services()
