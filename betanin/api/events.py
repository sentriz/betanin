from flask_socketio import emit
from betanin.extensions import socketio


def torrents_grabbed():
    socketio.emit('grabbed')


def line_read(torrent_id, index, line):
    payload = {
        # js case
        'torrentID': torrent_id,
        'index': index,
        'line': line,
    }
    socketio.emit('read', payload)
