# 3rd party
from flask_restplus import abort
from flask_jwt_extended import create_access_token

# betanin
from betanin import main_config
from betanin.rest.base import BaseResource
from betanin.rest.models import request as req_models
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import AUTHENTICATION_NS


@AUTHENTICATION_NS.route("/login")
class LoginResource(BaseResource):
    @staticmethod
    @AUTHENTICATION_NS.doc(parser=req_models.CREDENTIALS)
    @AUTHENTICATION_NS.doc(security=None)
    @AUTHENTICATION_NS.response(422, "invalid username / password")
    @AUTHENTICATION_NS.marshal_list_with(resp_models.AUTH_TOKEN)
    def post():
        "generates a json web token for the given username / password"
        args = req_models.CREDENTIALS.parse_args()
        config = main_config.read()
        if not main_config.credentials_correct(
            args["username"], args["password"]
        ):
            abort(422, "invalid username / password")
            return
        return {"token": create_access_token(args["username"])}
