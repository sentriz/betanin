# standard library
from functools import wraps

# 3rd party
from flask import abort
from flask import request
from flask_restplus import Resource
from flask_jwt_extended import verify_jwt_in_request

# betanin
from betanin import main_config


def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        if not api_key:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        if main_config.api_key_correct(api_key):
            return fn(*args, **kwargs)
        abort(422, "no valid auth provided")

    return wrapper


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = (auth_required,)
