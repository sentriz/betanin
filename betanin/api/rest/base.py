# 3rd party
from flask_restplus import Resource

# betanin
from betanin.api.security import require_auth


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = [require_auth]
