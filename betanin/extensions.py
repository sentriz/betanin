from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_restplus import Api
from flask_cors import CORS
from flask_migrate import Migrate


db = SQLAlchemy()
rest = Api()
socketio = SocketIO(
    # engineio_logger=True,
    # logger=True,
    async_mode='gevent',
)
cors = CORS()
migrate = Migrate()
