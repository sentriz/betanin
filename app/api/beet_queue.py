from collections import deque
from threading import Condition
import time
import eventlet


QUEUE = deque()
CV = Condition()


def _worker():
    while True:
        with CV:
            CV.wait_for(_are_torrents)
            t = _get_task()
            print('have', t)


def _are_torrents():
    return bool(QUEUE)


def _get_task():
    return QUEUE.popleft()


def add_torrent(torrent):
    with CV:
        QUEUE.append(torrent)
        CV.notify()


def start_worker():
    print("starting beets worker")
    eventlet.spawn(_worker)
