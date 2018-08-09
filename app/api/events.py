from flask_socketio import emit
import app


def torrents_grabbed():
    emit('torrents_grabbed')
