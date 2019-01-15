# standard library
from functools import wraps

# 3rd party
from flask import request
from flask_restplus import abort


def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers.get('authorization'):
            return func(*args, **kwargs)
        else:
            return abort(401)
    return wrapper
