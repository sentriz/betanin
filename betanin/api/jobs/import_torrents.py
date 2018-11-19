import pexpect
from contextlib import suppress
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


PROCESSES = {}
QUEUE = Queue()


def _add_line(torrent, index, data):
    torrent.add_line(index, data)
    db.session.commit()
    events.line_read(torrent.id, index, data)


def _calc_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _read_and_send_pty_out(proc, torrent):
    index = 0
    while True:
        try:
            data = proc.read_nonblocking(1024, 0.05)
        except pexpect.exceptions.TIMEOUT:
            gevent.sleep(1)
            continue
        except pexpect.exceptions.EOF:
            break
        text = data.decode()
        _add_line(torrent, index, text)
        index += 1


def _import_torrent(torrent):
    torrent.delete_lines()
    _add_line(torrent, -1, '[betanin] starting cli program')
    proc = pexpect.spawn('/home/senan/dev/repos/betanin/scripts/mock_beets', use_poll=True)
    PROCESSES[torrent.id] = proc
    _read_and_send_pty_out(proc, torrent)
    _add_line(torrent, 2**22, '[betanin] program finished with '
        f'exit status `{proc.exitstatus}`')
    return proc.exitstatus


def send_input(torrent_id, text):
    PROCESSES[torrent_id].sendline(text)


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
