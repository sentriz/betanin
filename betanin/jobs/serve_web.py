# 3rd party
import gevent
from loguru import logger
from gevent.pywsgi import WSGIServer


def start(flask_app, port):
    http_server = WSGIServer(("", port), log=None, application=flask_app)
    logger.info(f"starting wsgi server on port {port}")
    return gevent.spawn(http_server.start)
