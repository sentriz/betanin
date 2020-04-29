# standard library
import datetime

# 3rd party
from flask import abort

# betanin
from betanin import beets
from betanin.rest.base import SecureResource
from betanin.rest_models import request as req_models
from betanin.rest_models import response as resp_models
from betanin.rest.namespaces import BEETS_NS


@BEETS_NS.route("/config")
class BeetsResource(SecureResource):
    @staticmethod
    @BEETS_NS.marshal_list_with(resp_models.BEETS_CONFIG)
    def get():
        "reads the beets config from disk"
        config = beets.get_config()
        if not config:
            return abort(400, "config does not exist")
        return {"time_read": datetime.datetime.now(), "config": config}

    @staticmethod
    @BEETS_NS.doc(parser=req_models.BEETS_CONFIG)
    def put():
        "update the beets config on disk"
        args = req_models.BEETS_CONFIG.parse_args()
        beets.set_config(args["config"])
