# betanin
from betanin.api import notifications
from betanin.api.rest.base import BaseResource
from betanin.api.rest.models import request as req_models
from betanin.api.rest.models import response as resp_models
from betanin.api.rest.namespaces import notifications_ns


@notifications_ns.route('/services')
class ServicesResource(BaseResource):
    @staticmethod
    @notifications_ns.marshal_list_with(resp_models.notification_service)
    def get():
        'gets all notification services'
        return [
            {'id': id_, **service}
            for id_, service in \
                notifications.get_services().items()
        ]

    @staticmethod
    @notifications_ns.doc(parser=req_models.notification_service_type)
    @notifications_ns.marshal_with(resp_models.notification_service)
    def post():
        'creates template for new service'
        args = req_models.notification_service_type.parse_args()
        type_ = args['type']
        return notifications.add_service(type_)

    @staticmethod
    @notifications_ns.doc(parser=req_models.notification_service_list)
    def put():
        'updates all services'
        args = req_models.notification_service_list.parse_args()
        services = args['services']
        notifications.update_services({
            service.pop('id'): service
            for service in services
        })


@notifications_ns.route('/test_services')
class TestServicesResource(BaseResource):
    @staticmethod
    @notifications_ns.marshal_with(resp_models.notification_test_result)
    def get():
        'tests the saved notifications'
        return {
            "result": notifications.test_services(),
        }


@notifications_ns.route('/possible_services')
class PossibleServicesResource(BaseResource):
    @staticmethod
    def get():
        'gets all possible notification services'
        return notifications.get_possible_services()


@notifications_ns.route('/general')
class GeneralResource(BaseResource):
    @staticmethod
    @notifications_ns.marshal_with(resp_models.notification_settings)
    def get():
        'gets your saved notification services'
        return notifications.get_general()

    @staticmethod
    @notifications_ns.doc(parser=req_models.notification_general)
    def put():
        'updates a notification service'
        args = req_models.notification_general.parse_args()
        notifications.update_general(args)
