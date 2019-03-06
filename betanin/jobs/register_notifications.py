# betanin
from betanin import notifications
from betanin.extensions import socketio


def start(flask_app):
    return socketio.start_background_task(notifications.register_all)
