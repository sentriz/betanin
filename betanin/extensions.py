# standard library
import os

# 3rd party
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restplus import Api
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
rest = Api(
    version=os.environ.get('SOURCE_COMMIT', 'development'),
    title='betanin\'s rest api',
    description='see https://github.com/sentriz/betanin for more',
)
socketio = SocketIO(
    # engineio_logger=True,
    # logger=True,
    async_mode='gevent',
)
