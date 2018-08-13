from gevent import monkey
monkey.patch_all()


from flask import Flask

from betanin import api
from betanin import client
from betanin import commands
from betanin.config.flask import config_from_string
from betanin.extensions import db
from betanin.extensions import rest
from betanin.extensions import socketio


def create_app(config_name="development"):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    config_obj = config_from_string(config_name)
    app.config.from_object(config_obj)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    socketio.init_app(app)


def register_blueprints(app):
    # api blueprint & extensions (first)
    rest.init_app(api.blueprint)
    app.register_blueprint(api.blueprint)
    # client "
    app.register_blueprint(client.blueprint)


def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
