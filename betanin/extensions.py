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
    "jwt": {"type": "apiKey", "in": "header", "name": "Authorization"}
}
cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
rest = Api(
    version=version.__version__,
    title="betanin's rest api",
    description="see https://github.com/sentriz/betanin for more",
    authorizations=_rest_authorisations,
    security="jwt",
)
socketio = SocketIO(
    # engineio_logger=True,
    # logger=True,
    async_mode="gevent"
)
jwt = JWTManager()
