from queue import Queue
import subprocess

from betanin.api import events
from betanin.api.models.torrent import Torrent
from betanin.extensions import db
from betanin.extensions import scheduler

import gevent


QUEUE = Queue()
PROCESSES = {}


def _print_wait(time):
    for n in range(time):
        print('||| prog', n)
        gevent.sleep(1)


def add(torrent):
    QUEUE.put(torrent)


def import_torrent(torrent):
    torrent.delete_lines()
    proc = subprocess.Popen(
        "/home/senan/dev/repos/betanin/scripts/mock_beets",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )
    PROCESSES[torrent.id] = proc
    for i, raw_line in enumerate(iter(p.stdout.readline, b'')):
        data = raw_line.rstrip()
        torrent.add_line(i, data)
        events.line_read(torrent.id, i, data)
        db.session.commit()
    proc.stdout.close()
    proc.wait()


def _torrent_from_id(torrent_id):
    return db.session.query(Torrent).get(torrent_id)


def start():
    with scheduler.app.app_context():
        while True:
            torrent_id = QUEUE.get()
            torrent = _torrent_from_id(torrent_id)
            torrent.set_beta_status("processing")
            db.session.commit()
            import_torrent(torrent)
            torrent.set_beta_status("completed")
            db.session.commit()
            QUEUE.task_done()
