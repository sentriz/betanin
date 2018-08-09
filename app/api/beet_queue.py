from collections import deque
from threading import Thread
from threading import Condition
import time


QUEUE = deque()
CV = Condition()


def _consume():
    print("starting queue worker")
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
    thread = Thread(target=_consume)
    thread.start()
