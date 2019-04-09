# betanin
from betanin import system_info
from betanin.rest.base import SecureResource
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import meta_ns


@meta_ns.route("/system_info")
class metaResource(SecureResource):
    @staticmethod
    @meta_ns.marshal_with(resp_models.system_info)
    def get():
        "gets the current system info"
        return system_info.SYSTEM_INFO
