# betanin
from betanin import notifications
from betanin.rest.base import SecureResource
from betanin.rest_models import request as req_models
from betanin.rest_models import response as resp_models
from betanin.rest.namespaces import NOTIFICATIONS_NS


@NOTIFICATIONS_NS.route("/services")
class ServicesResource(SecureResource):
    @staticmethod
    @NOTIFICATIONS_NS.marshal_list_with(resp_models.NOTIFICATION_SERVICE)
    def get():
        "gets all notification services"
        return [
            {"id": id_, **service}
            for id_, service in notifications.get_services().items()
        ]

    @staticmethod
    @NOTIFICATIONS_NS.doc(parser=req_models.NOTIFICATION_SERVICE_TYPE)
    @NOTIFICATIONS_NS.marshal_with(resp_models.NOTIFICATION_SERVICE)
    def post():
        "creates template for new service"
        args = req_models.NOTIFICATION_SERVICE_TYPE.parse_args()
        type_ = args["type"]
        return notifications.add_service(type_)

    @staticmethod
    @NOTIFICATIONS_NS.doc(parser=req_models.NOTIFICATION_SERVICE_LIST)
    def put():
        "updates all services"
        args = req_models.NOTIFICATION_SERVICE_LIST.parse_args()
        services = args["services"]
        notifications.update_services(
            {service.pop("id"): service for service in services}
        )


@NOTIFICATIONS_NS.route("/test_services")
class TestServicesResource(SecureResource):
    @staticmethod
    @NOTIFICATIONS_NS.marshal_with(resp_models.NOTIFICATION_TEST_RESULT)
    def get():
        "tests the saved notifications"
        return {"result": notifications.test_services()}


@NOTIFICATIONS_NS.route("/possible_services")
class PossibleServicesResource(SecureResource):
    @staticmethod
    def get():
        "gets all possible notification services"
        return notifications.get_possible_services()


@NOTIFICATIONS_NS.route("/strings")
class StringsResource(SecureResource):
    @staticmethod
    @NOTIFICATIONS_NS.marshal_with(resp_models.NOTIFICATION_SETTINGS)
    def get():
        "gets your saved notification services"
        return notifications.get_strings()

    @staticmethod
    @NOTIFICATIONS_NS.doc(parser=req_models.NOTIFICATION_STRINGS)
    def put():
        "updates a notification service"
        args = req_models.NOTIFICATION_STRINGS.parse_args()
        notifications.update_strings(args)
