__import__('eventlet').monkey_patch()

import os

from app.api import api_rest
from app.api import api_bp
from app.client import client_bp

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


# base
app = Flask(__name__)
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

# config (before the extras)
_config_type = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object(f'app.flask_config.{_config_type}')

# orm
db = SQLAlchemy(app)

# socketio (last)
socketio = SocketIO(
    app,
    # engineio_logger=True,
    # logger=True,
    async_mode='eventlet',
)
