from flask_socketio import emit
import betanin


def torrents_grabbed():
    app.socketio.emit('grabbed')
