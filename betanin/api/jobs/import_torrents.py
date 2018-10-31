from gevent.queue import Queue
import gevent
import subprocess

import re
import os.path

from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.extensions import db
from betanin.api.status import Status


PROCESSES = {}
QUEUE = Queue()


def _add_line(torrent, index, data):
    torrent.add_line(index, data)
    db.session.commit()
    events.line_read(torrent.id, index, data)


def _calc_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _import_torrent(torrent):
    torrent.delete_lines()
    _add_line(torrent, -1, '[betanin] starting cli program')
    proc = subprocess.Popen(
        ['sleep', '200'],
        # ['beet', 'import', '-c', _calc_import_path(torrent)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )
    PROCESSES[torrent.id] = proc
    for i, raw_line in enumerate(iter(proc.stdout.readline, '')):
        # TODO: add regex here to update status to
        # possibly update NEEDS_INPUT
        data = raw_line.rstrip()
        print(i, data)
        _add_line(torrent, i, data)
    proc.stdout.close()
    proc.wait()
    return_code = proc.returncode
    _add_line(torrent, 2*22, '[betanin] program finished with '
        f'exit status `{return_code}`')
    return return_code


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
