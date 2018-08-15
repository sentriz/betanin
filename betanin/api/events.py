from flask_socketio import emit
from betanin.extensions import socketio


def torrents_grabbed():
    socketio.emit('grabbed')
