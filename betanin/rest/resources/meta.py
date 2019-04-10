# betanin
from betanin import system_info
from betanin.rest.base import SecureResource
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import META_NS


@META_NS.route("/system_info")
class metaResource(SecureResource):
    @staticmethod
    @META_NS.marshal_with(resp_models.SYSTEM_INFO)
    def get():
        "gets the current system info"
        return system_info.SYSTEM_INFO
