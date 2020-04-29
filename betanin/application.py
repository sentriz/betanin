# 3rd party
import sqlalchemy_utils
from flask import Flask
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix

# betanin
import betanin.config.flask as conf_flask
import betanin.config.secret_key as conf_secret_key
from betanin import blueprints
from betanin.models import Line  # noqa
from betanin.models import Torrent  # noqa
from betanin.extensions import DB
from betanin.extensions import JWT
from betanin.extensions import CORS
from betanin.extensions import REST
from betanin.extensions import MIGRATE
from betanin.extensions import SOCKETIO
from betanin.rest_resources import meta  # noqa
from betanin.rest_resources import beets  # noqa
from betanin.rest_resources import torrents  # noqa
from betanin.rest_resources import notifications  # noqa
from betanin.rest_resources import authentication  # noqa
from betanin.rest_resources import torrent_clients  # noqa


def create():
    app = Flask("betanin")
    register_modifications(app)
    register_extensions(app)
    register_cors(app)
    register_routes(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    sqlalchemy_utils.force_instant_defaults()
    sqlalchemy_utils.force_auto_coercion()
    DB.init_app(app)
    CORS.init_app(app)
    MIGRATE.init_app(app, DB)
    SOCKETIO.init_app(app)
    JWT.init_app(app)
    JWT._set_error_handler_callbacks(REST)


def register_cors(app):
    _origins = app.config.get("CORS_ORIGIN_WHITELIST", "*")
    CORS.init_app(blueprints.API, origins=_origins)
    CORS.init_app(blueprints.CLIENT, origins=_origins)


def register_routes(app):
    # the client blueprint has one route which is the
    # the built frontend
    render_client = lambda: render_template("index.html")
    blueprints.CLIENT.route("/")(render_client)
    # the api blueprint has many routes which are handled
    # by flask-restplus
    REST.init_app(blueprints.API)


def register_blueprints(app):
    app.register_blueprint(blueprints.CLIENT)
    app.register_blueprint(blueprints.API)


def register_modifications(app):
    app.config.from_object(conf_flask)
    app.url_map.strict_slashes = False
    app.secret_key = conf_secret_key.read()
    app.wsgi_app = ProxyFix(app.wsgi_app)
