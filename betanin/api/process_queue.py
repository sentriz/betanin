import gevent
from flask import copy_current_request_context

from queue import Queue
import subprocess

from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.extensions import db
from betanin.extensions import scheduler
from betanin.api.status import BetaStatus
from betanin.api.torrent_client import calc_import_path


QUEUE = Queue()
PROCESSES = {}


def add(torrent):
    QUEUE.put(torrent)


def import_torrent(torrent):
    torrent.delete_lines()
    proc = subprocess.Popen(
        ['beet', 'import', '-c',
            calc_import_path(torrent.remote.id, torrent.path, torrent.name)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )
    PROCESSES[torrent.id] = proc
    for i, raw_line in enumerate(iter(proc.stdout.readline, '')):
        # TODO: add regex here to update beta_status to
        # possibly update NEEDS_INPUT
        data = raw_line.rstrip()
        torrent.add_line(i, data)
        events.line_read(torrent.id, i, data)
        db.session.commit()
    proc.stdout.close()
    proc.wait()
    return proc


def _torrent_from_id(torrent_id):
    return db.session.query(Torrent).get(torrent_id)


def _start():
    while True:
        torrent_id = QUEUE.get()
        torrent = _torrent_from_id(torrent_id)
        torrent.set_status(BetaStatus.PROCESSING)
        db.session.commit()
        proc = import_torrent(torrent)
        if proc.returncode == 0:
            torrent.set_status(BetaStatus.COMPLETED)
        else:
            torrent.set_status(BetaStatus.FAILED)
        db.session.commit()
        QUEUE.task_done()


def start():
    gevent.spawn(_start)
