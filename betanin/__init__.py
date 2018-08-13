from gevent import monkey
monkey.patch_all()


from flask import Flask

from betanin.extensions import db
from betanin.extensions import rest
from betanin.extensions import socketio


def create_app():
    app = Flask(__name__)
    _config_env = os.environ.get('FLASK_CONFIG', 'Development')
    app.config.from_object(f'betanin.flask_config.{_config_env}')
    db.init_app(app)
    rest.init_app(app)
    socketio.init_app(app)
    return app
