# 3rd party
import gevent
from gevent.pywsgi import WSGIServer


def start(flask_app, host, port):
    http_server = WSGIServer((host, port), log=None, application=flask_app)
    return gevent.spawn(http_server.start)
