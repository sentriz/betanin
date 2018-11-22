# 3rd party
import gevent

# betanin
from betanin.api import notifications
from betanin.extensions import socketio


def send_torrents_changed():
    socketio.emit('changed')


def send_line_read(torrent_id, index, data):
    socketio.emit('read', {
        # js case
        'torrentID': torrent_id,
        'line': {
            'index': index,
            'data': data,
        }
    })


def send_torrent_status_changed(torrent):
    gevent.spawn(notifications.send, torrent)
