# from gevent import monkey
# monkey.patch_all()


from flask import Flask

from betanin import api
from betanin import client
from betanin import commands
from betanin.config.flask import config_from_string
from betanin.extensions import db
from betanin.extensions import rest
from betanin.extensions import socketio
from betanin.extensions import cors
from betanin.extensions import migrate


def create_app(config_name="development"):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    config_obj = config_from_string(config_name)
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)


def register_blueprints(app):
    # blueprint extensions (before register)
    rest.init_app(api.blueprint)
    _origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(api.blueprint, origins=_origins)
    cors.init_app(api.blueprint, origins=_origins)
    # blueprints
    app.register_blueprint(api.blueprint)
    app.register_blueprint(client.blueprint)


def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
