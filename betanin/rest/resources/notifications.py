# betanin
from betanin import notifications
from betanin.rest.base import SecureResource
from betanin.rest.models import request as req_models
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import notifications_ns


@notifications_ns.route('/services')
class ServicesResource(SecureResource):
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
class TestServicesResource(SecureResource):
    @staticmethod
    @notifications_ns.marshal_with(resp_models.notification_test_result)
    def get():
        'tests the saved notifications'
        return {
            "result": notifications.test_services(),
        }


@notifications_ns.route('/possible_services')
class PossibleServicesResource(SecureResource):
    @staticmethod
    def get():
        'gets all possible notification services'
        return notifications.get_possible_services()


@notifications_ns.route('/strings')
class stringsResource(SecureResource):
    @staticmethod
    @notifications_ns.marshal_with(resp_models.notification_settings)
    def get():
        'gets your saved notification services'
        return notifications.get_strings()

    @staticmethod
    @notifications_ns.doc(parser=req_models.notification_strings)
    def put():
        'updates a notification service'
        args = req_models.notification_strings.parse_args()
        notifications.update_strings(args)
