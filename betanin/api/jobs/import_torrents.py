from gevent.queue import Queue
import gevent
import subprocess

import re

from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.extensions import db
from betanin.api.status import Status


ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
PROCESSES = {}
QUEUE = Queue()


def _clean_line(line):
    return ANSI_ESCAPE.sub('', line)


def _add_line(torrent, index, data):
    torrent.add_line(index, data)
    db.session.commit()
    events.line_read(torrent.id, index, data)


def _import_torrent(torrent):
    torrent.delete_lines()
    _add_line(torrent, -1, '[betanin] starting beets cli..')
    proc = subprocess.Popen(
        ['beet', 'import', '-c', torrent.path],
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
        data = _clean_line(raw_line.rstrip())
        _add_line(torrent, i, data)
    proc.stdout.close()
    proc.wait()
    return proc


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
        proc = _import_torrent(torrent)
        if proc.returncode == 0:
            torrent.status = Status.PROCESSED
        else:
            torrent.status = Status.FAILED
        db.session.commit()
        events.torrents_changed()
