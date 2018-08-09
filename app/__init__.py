__import__('eventlet').monkey_patch()

import os

from app.api import api_rest
from app.api import api_bp
from app.client import client_bp

from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)

app.register_blueprint(api_bp)
app.register_blueprint(client_bp)


from . import config


socketio = SocketIO(
    app,
    # engineio_logger=True,
    # logger=True,
    async_mode='eventlet',
)
