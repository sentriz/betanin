from collections import deque
from threading import Condition
import time

from betanin.api.status import BetaStatus
from betanin.extensions import scheduler

QUEUE = deque()
CV = Condition()


def _are_torrents():
    return bool(QUEUE)


def _get_task():
    return QUEUE.popleft()


def _add(torrent):
    with CV:
        QUEUE.append(torrent)
        torrent.status = BetaStatus.ENQUEUED
        CV.notify()


def start():
    scheduler.app.app_context().push()
    while True:
        with CV:
            CV.wait_for(_are_torrents)
            torrent = _get_task()
            # torrent.status = BetaStatus.PROCESSING
            print('have', torrent)
            gevent.sleep(10)
            # torrent.status = BetaStatus.COMPLETED
