from queue import Queue
import gevent
import time

from betanin.extensions import scheduler
from betanin.api.status import BetaStatus

import gevent


QUEUE = Queue()


def _print_wait(time):
    for n in range(time):
        print('||| prog', n)
        gevent.sleep(1)


def add(torrent):
    QUEUE.put(torrent)
    torrent.beta_status = BetaStatus.ENQUEUED


def start():
    scheduler.app.app_context().push()
    while True:
        torrent = QUEUE.get()
        torrent.beta_status = BetaStatus.PROCESSING
        print(f'/// have torrent {torrent.id}')
        _print_wait(10)
        torrent.beta_status = BetaStatus.COMPLETED
        print(f'\\\\ finished torrent {torrent.id}')
        QUEUE.task_done()
