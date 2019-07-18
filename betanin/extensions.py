# 3rd party
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restplus import Api
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# betanin
from betanin import version


_rest_authorisations = {
    "jwt": {"type": "apiKey", "in": "header", "name": "Authorization"},
    "api key": {"type": "apiKey", "in": "header", "name": "X-API-Key"},
}

# loading swagger.json mixed content fix
Api.specs_url = "/api/swagger.json"

# uninitialised extensions
CORS = CORS()
DB = SQLAlchemy()
MIGRATE = Migrate()
REST = Api(
    version=version.__version__,
    title="betanin's rest api",
    description="see https://github.com/sentriz/betanin for more",
    authorizations=_rest_authorisations,
    security=["jwt", "api key"],
)
SOCKETIO = SocketIO(
    # engineio_logger=True,
    # logger=True,
    async_mode="gevent"
)
JWT = JWTManager()
