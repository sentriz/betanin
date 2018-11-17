# python
import os.path
import subprocess
import sys
import pty
import select

# 3rd party
import gevent
from gevent.queue import Queue

# betanin
from betanin.api import events
from betanin.api.status import Status
from betanin.extensions import db
from betanin.extensions import socketio
from betanin.api.orm.models.torrent import Torrent


DESCIPTOR = None
QUEUE = Queue()


def _add_line(torrent, index, data):
    torrent.add_line(index, data)
    db.session.commit()
    events.line_read(torrent.id, index, data)


def _calc_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _read_and_forward_pty_output(torrent, descriptor):
    index = 0
    while True:
        gevent.sleep(0.01)
        if not descriptor:
            break
        data_ready, _, _ = select.select([descriptor], [], [], 0)
        if not data_ready:
            continue
        output = os.read(descriptor, 1024 * 20).decode()
        _add_line(torrent, index, output)
        index += 1


def _import_torrent(torrent):
    global DESCIPTOR
    torrent.delete_lines()
    _add_line(torrent, -1, '[betanin] starting cli program')
    child_pid, descriptor = pty.fork()
    if child_pid == 0:
        DESCIPTOR = descriptor
        proc = subprocess.run("/home/senan/dev/repos/betanin/scripts/mock_beets")
        proc.wait()
        sys.exit()
    else:
        _read_and_forward_pty_output(torrent, descriptor)
        _add_line(torrent, 2**22, '[betanin] program finished with '
            f'exit status `{return_code}`')


def send_input(text):
    os.write(DESCIPTOR, text)


def add(**kwargs):
    torrent = Torrent(**kwargs)
    torrent.status = Status.ENQUEUED
    # add and commit the new torrent because the queue
    # and socket/ajax event will need them to be
    db.session.add(torrent)
    db.session.commit()
    # add to queue
    QUEUE.put_nowait(torrent.id)
    # tell client to get latest torrents
    events.torrents_changed()


def start():
    while True:
        torrent_id = QUEUE.get()
        torrent = Torrent.query.get(torrent_id)
        torrent.status = Status.PROCESSING
        db.session.commit()
        events.torrents_changed()
        return_code = _import_torrent(torrent)
        if return_code == 0:
            torrent.status = Status.COMPLETED
        else:
            torrent.status = Status.FAILED
        db.session.commit()
        events.torrents_changed()
