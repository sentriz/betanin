from queue import Queue
import subprocess

from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.extensions import db
from betanin.extensions import scheduler
from betanin.api.status import BetaStatus


QUEUE = Queue()
PROCESSES = {}


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
    for i, raw_line in enumerate(iter(proc.stdout.readline, '')):
        # TODO: add regex here to update beta_status to
        # possibly update NEEDS_INPUT
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
            torrent.set_status(BetaStatus.PROCESSING)
            db.session.commit()
            import_torrent(torrent)
            torrent.set_status(BetaStatus.COMPLETED)
            db.session.commit()
            QUEUE.task_done()
