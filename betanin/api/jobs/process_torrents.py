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
    return Torrent.query.filter_by(id=torrent_id)


def start():
    scheduler.app.app_context().push()
    while True:
        torrent_id = QUEUE.get()
        torrent = _torrent_from_id(torrent_id)
        # db.session.query(Torrent).filter_by(id=torrent_id).update(
        #     {
        #         'beta_status': BetaStatus.PROCESSING
        #     }
        # )
        torrent.update({
            'beta_status': BetaStatus.PROCESSING
        })
        print(f'/// have torrent')
        _print_wait(10)
        torrent.update({
            'beta_status': BetaStatus.COMPLETED
        })
        print(f'\\\\ finished torrent')
        QUEUE.task_done()
