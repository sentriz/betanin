# 3rd party
from flask_restplus import marshal

# betanin
from betanin.extensions import socketio
from betanin.rest.models import response


def send_torrent(torrent):
    socketio.emit("newTorrent", marshal(torrent, response.torrent))


def send_line(line):
    socketio.emit("newLine", marshal(line, response.line_with_torrent_id))
