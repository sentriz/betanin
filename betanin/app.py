from gevent import monkey; monkey.patch_all()

from flask import Flask
import atexit

from betanin import api
from betanin import client
from betanin import commands
from betanin.api import process_queue
from betanin.api import torrent_client
from betanin.config import config_from_string
from betanin.extensions import cors
from betanin.extensions import db
from betanin.extensions import migrate
from betanin.extensions import rest
from betanin.extensions import scheduler
from betanin.extensions import socketio


def create_app(config_name="development"):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    config_obj = config_from_string(config_name)
    app.config.from_object(config_obj)
    register_commands(app)
    register_extensions(app)
    register_blueprints(app)
    register_meta(app)
    return app


def register_extensions(app):
    # orm
    db.init_app(app)
    # cors
    cors.init_app(app)
    from sqlalchemy_utils import force_instant_defaults
    force_instant_defaults()
    # scheduler
    scheduler.init_app(app)
    # migrations
    from betanin.api.orm.models.torrent import Torrent
    from betanin.api.orm.models.line import Line
    from betanin.api.orm.models.remote import Remote
    migrate.init_app(app, db)
    # socketio
    socketio.init_app(app)


def register_blueprints(app):
    # blueprint extensions (before register)
    rest.init_app(api.blueprint)
    _origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(api.blueprint, origins=_origins)
    cors.init_app(client.blueprint, origins=_origins)
    # blueprints
    app.register_blueprint(api.blueprint)
    app.register_blueprint(client.blueprint)


def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.clean)


def register_meta(app):
    # if os.environ['FLASK_RUN_FROM_CLI'] == 'true':
    #     return
    with app.app_context():
        torrent_client.make_all_sessions()
        process_queue.start(app)
    scheduler.start()
    atexit.register(scheduler.shutdown)
