from collections import deque
from threading import Condition
import time
import eventlet
from app.api.torrent import RemoteStatus
from app.api.torrent import BetaStatus


QUEUE = deque()
CV = Condition()


def _worker():
    while True:
        with CV:
            CV.wait_for(_are_torrents)
            torrent = _get_task()
            torrent.status = BetaStatus.PROCESSING
            print('have', torrent)
            eventlet.sleep(10)
            torrent.status = BetaStatus.COMPLETED


def _are_torrents():
    return bool(QUEUE)


def _get_task():
    return QUEUE.popleft()


def add(torrent):
    with CV:
        QUEUE.append(torrent)
        torrent.status = BetaStatus.ENQUEUED
        CV.notify()


def start_worker():
    print("starting beets worker")
    eventlet.spawn(_worker)
