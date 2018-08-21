from flask_restplus import Resource

from betanin.api.security import require_auth


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = [require_auth]
