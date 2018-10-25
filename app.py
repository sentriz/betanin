#!/usr/bin/env python3

from gevent import monkey; monkey.patch_all()
import gevent

from flask import Flask

from betanin import api
from betanin import client
from betanin.config import Config
from betanin.api import jobs
from betanin.api import torrent_client
from betanin.api.jobs import fetch_torrents
from betanin.api.jobs import import_torrents
from betanin.api.tasks import make_all_sessions
from betanin.extensions import cors
from betanin.extensions import db
from betanin.extensions import migrate
from betanin.extensions import rest
from betanin.extensions import socketio


def create_app():
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    # orm
    db.init_app(app)
    # cors
    cors.init_app(app)
    from sqlalchemy_utils import force_instant_defaults
    force_instant_defaults()
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
    app.register_blueprint(client.blueprint)
    app.register_blueprint(api.blueprint)


if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    flask_app = create_app()
    def _make_starter(module):
        def _context_wrapper():
            with flask_app.app_context():
                module.start()
        return _context_wrapper
    # tasks
    init_tasks = (
        _make_starter(make_all_sessions),
    )
    # jobs
    _http_server = WSGIServer(('', 5000), log=None, application=flask_app)
    http_server_job = gevent.spawn(_http_server.start)
    extra_jobs = map(gevent.spawn, (
        _make_starter(fetch_torrents),
        _make_starter(import_torrents),
    ))
    try:
        # start init tasks
        [task() for task in init_tasks]
        # start http job and extra jobs
        gevent.joinall((http_server_job, *extra_jobs))
    except KeyboardInterrupt:
        print('exiting')
