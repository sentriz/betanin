from flask_socketio import emit
import app


def torrents_grabbed():
    app.socketio.emit('grabbed')
