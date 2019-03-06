#!/usr/bin/env python3

from gevent import monkey; monkey.patch_all()

# 3rd party
import sqlalchemy_utils
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

# betanin
from betanin import blueprints
from betanin import secret_key
from betanin import flask_config
from betanin.extensions import db
from betanin.extensions import jwt
from betanin.extensions import cors
from betanin.extensions import rest
from betanin.extensions import migrate
from betanin.extensions import socketio
from betanin.rest.resources import meta  # noqa
from betanin.rest.resources import beets  # noqa
from betanin.rest.resources import torrents  # noqa
from betanin.rest.resources import notifications  # noqa
from betanin.rest.resources import authentication  # noqa
from betanin.rest.resources import torrent_clients  # noqa
from betanin.orm.models.line import Line  # noqa
from betanin.orm.models.torrent import Torrent  # noqa


def create():
    app = Flask(__name__.split('.')[0])
    register_modifications(app)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    sqlalchemy_utils.force_instant_defaults()
    sqlalchemy_utils.force_auto_coercion()
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    jwt.init_app(app)
    jwt._set_error_handler_callbacks(rest)


def register_blueprints(app):
    # blueprint extensions (before register)
    rest.init_app(blueprints.api)
    _origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(blueprints.api, origins=_origins)
    cors.init_app(blueprints.client, origins=_origins)
    # blueprints
    app.register_blueprint(blueprints.client)
    app.register_blueprint(blueprints.api)


def register_modifications(app):
    app.config.from_object(flask_config)
    app.url_map.strict_slashes = False
    app.secret_key = secret_key.read()
    app.wsgi_app = ProxyFix(app.wsgi_app)
