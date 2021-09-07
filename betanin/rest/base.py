# standard library
from functools import wraps

# 3rd party
from flask import abort
from flask import request
from flask_restplus import Resource
from flask_jwt_extended import verify_jwt_in_request

# betanin
import betanin.config.betanin as conf_betanin


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        if not api_key:
            verify_jwt_in_request()
            return func(*args, **kwargs)
        conf = conf_betanin.read()
        if conf_betanin.find_api_key_correct(conf, api_key):
            return func(*args, **kwargs)
        return abort(422, "no valid auth provided")

    return wrapper


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = (auth_required,)
