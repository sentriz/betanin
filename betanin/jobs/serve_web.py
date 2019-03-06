# 3rd party
from loguru import logger
from gevent.pywsgi import WSGIServer

# betanin
from betanin.extensions import socketio


def start(flask_app, port):
    http_server = WSGIServer(('', port), log=None, application=flask_app)
    logger.info(f'starting wsgi server on port {port}')
    return socketio.start_background_task(http_server.start)
