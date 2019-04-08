# 3rd party
import gevent

# betanin
from betanin import notifications


def start(flask_app):
    return gevent.spawn(notifications.register_all)
