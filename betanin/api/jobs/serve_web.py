# 3rd party
from gevent.pywsgi import WSGIServer

# betanin
from betanin.extensions import socketio


def start(flask_app):
    http_server = WSGIServer(('', 5000), log=None, application=flask_app)
    return socketio.start_background_task(http_server.start)
