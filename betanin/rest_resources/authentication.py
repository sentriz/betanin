# 3rd party
from flask_restplus import abort
from flask_jwt_extended import create_access_token

# betanin
import betanin.config.betanin as conf_betanin
from betanin.rest.base import BaseResource
from betanin.rest_models import request as req_models
from betanin.rest_models import response as resp_models
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
        if not conf_betanin.credentials_correct(
            args["username"], args["password"]
        ):
            return abort(422, "invalid username / password")
        return {"token": create_access_token(args["username"])}
