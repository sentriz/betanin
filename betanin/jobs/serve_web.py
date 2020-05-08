# 3rd party
import gevent
from loguru import logger
from gevent.pywsgi import WSGIServer


def start(flask_app, host, port):
    http_server = WSGIServer((host, port), log=None, application=flask_app)
    logger.info(f"listening on port {port}")
    return gevent.spawn(http_server.start)
