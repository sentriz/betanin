# standard library
import os
from glob import glob

# betanin
from betanin import system_info
from betanin.rest.base import SecureResource
from betanin.rest_models import request as req_models
from betanin.rest_models import response as resp_models
from betanin.rest.namespaces import META_NS


@META_NS.route("/system_info")
class SystemInfoResource(SecureResource):
    @staticmethod
    @META_NS.marshal_with(resp_models.SYSTEM_INFO)
    def get():
        "gets the current system info"
        return system_info.SYSTEM_INFO


@META_NS.route("/sub_dirs")
class SubDirsResource(SecureResource):
    @staticmethod
    @META_NS.doc(parser=req_models.SUB_DIRS)
    @META_NS.marshal_list_with(resp_models.SUB_DIR)
    def get():
        "gets the sub directories of a provided one"
        args = req_models.SUB_DIRS.parse_args()
        path = os.path.expanduser(args["dir"])
        sub_paths = glob(path + "*")
        sub_dirs = filter(os.path.isdir, sub_paths)
        return [{"path": path} for path in sub_dirs]
