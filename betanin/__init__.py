from gevent import monkey
monkey.patch_all()

from flask import Flask
import os


def init_app():
    app = Flask(__name__)
    config_type = os.environ.get('FLASK_CONFIG', 'Development')
    app.config.from_object(f'betanin.flask_config.{config_type}')
    return app


def register_orm(app):
    from flask_sqlalchemy import SQLAlchemy
    return SQLAlchemy(app)


def register_socketio(app):
    from flask_socketio import SocketIO
    return SocketIO(
        app,
        # engineio_logger=True,
        # logger=True,
        async_mode='gevent',
    )


def register_blueprints(app):
    from betanin.api import api_bp
    from betanin.client import client_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(client_bp)
