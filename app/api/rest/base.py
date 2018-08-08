""" API Backend - Base Resource Models """

from flask_restplus import Resource, abort
from app.api.security import require_auth


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = [require_auth]
