# 3rd party
from flask_restplus import marshal

# betanin
from betanin.extensions import SOCKETIO
from betanin.rest_models import response


def send_torrent(torrent):
    SOCKETIO.emit("newTorrent", marshal(torrent, response.TORRENT))


def send_line(line):
    SOCKETIO.emit("newLine", marshal(line, response.LINE_WITH_TORRENT_ID))
