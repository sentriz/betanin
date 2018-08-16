from collections import deque
from threading import Condition
import time
import gevent

from betanin.api.status import BetaStatus
from betanin.extensions import scheduler
from betanin.extensions import db

QUEUE = deque()
CV = Condition()


def _are_torrents():
    return bool(QUEUE)


def _get_task():
    return QUEUE.popleft()


def add(torrent):
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
            print(f'HAVE HAVE TORRENT {torrent.id}')
            torrent.remote_status = BetaStatus.PROCESSING
            gevent.sleep(12)
            torrent.remote_status = BetaStatus.COMPLETED
