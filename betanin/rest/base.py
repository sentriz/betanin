# 3rd party
from flask_restplus import Resource
from flask_jwt_extended import jwt_required


class BaseResource(Resource):
    pass


class SecureResource(BaseResource):
    method_decorators = (jwt_required,)
