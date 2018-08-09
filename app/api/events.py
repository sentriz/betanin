from flask_socketio import emit
import app


def torrents_grabbed():
    app.socketio.emit('torrents_grabbed')
