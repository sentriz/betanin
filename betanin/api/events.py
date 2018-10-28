from betanin.extensions import socketio


def torrents_changed():
    socketio.emit('changed')


def line_read(torrent_id, index, data):
    socketio.emit('read', {
        # js case
        'torrentID': torrent_id,
        'line': {
            'index': index,
            'data': data,
        }
    })
