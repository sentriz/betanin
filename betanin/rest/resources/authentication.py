# 3rd party
from flask_restplus import abort
from flask_jwt_extended import create_access_token

# betanin
from betanin import main_config
from betanin.rest.base import BaseResource
from betanin.rest.models import request as req_models
from betanin.rest.models import response as resp_models
from betanin.rest.namespaces import authentication_ns


@authentication_ns.route('/login')
class LoginResource(BaseResource):
    @staticmethod
    @authentication_ns.doc(parser=req_models.credentials)
    @authentication_ns.doc(security=None)
    @authentication_ns.response(422, 'invalid username / password')
    @authentication_ns.marshal_list_with(resp_models.auth_token)
    def post():
        'generates a json web token for the given username / password'
        args = req_models.credentials.parse_args()
        config = main_config.read()
        if not main_config.credentials_correct(args['username'], args['password']):
            abort(422, 'invalid username / password')
            return
        return {
            "token": create_access_token(args['username'])
        }
