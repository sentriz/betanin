from queue import Queue
import time
import subprocess

from betanin.api import events
from betanin.api.models.torrent import Torrent
from betanin.api.status import BetaStatus
from betanin.extensions import db
from betanin.extensions import scheduler

import gevent


QUEUE = Queue()


def _print_wait(time):
    for n in range(time):
        print('||| prog', n)
        gevent.sleep(1)


def add(torrent):
    QUEUE.put(torrent)


def import_torrent(torrent):
    torrent.delete_lines()
    p = subprocess.Popen(
        "/home/senan/dev/repos/betanin/scripts/mock_beets",
        stdout=subprocess.PIPE,
        bufsize=1,
    )
    for i, raw_line in enumerate(iter(p.stdout.readline, b'')):
        line = raw_line.decode('utf-8').lstrip()
        torrent.add_line(i, line)
        events.line_read(torrent.id, i, line)
        db.session.commit()
        print(line)
    p.stdout.close()
    p.wait()


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
