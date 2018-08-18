from queue import Queue
import gevent
import time

from betanin.extensions import scheduler
from betanin.extensions import db
from betanin.api.status import BetaStatus
from betanin.api.models.torrent import Torrent

import gevent


QUEUE = Queue()


def _print_wait(time):
    for n in range(time):
        print('||| prog', n)
        gevent.sleep(1)


def add(torrent):
    QUEUE.put(torrent)


def _torrent_from_id(torrent_id):
    return db.session.query(Torrent).get(torrent_id)


def start():
    with scheduler.app.app_context():
        while True:
            torrent_id = QUEUE.get()
            torrent = _torrent_from_id(torrent_id)
            torrent.set_beta_status("processing")
            db.session.commit()
            print(f'/// have torrent')
            _print_wait(10)
            print(f'\\\\ finished torrent')
            torrent.set_beta_status("completed")
            db.session.commit()
            QUEUE.task_done()
