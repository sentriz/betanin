from collections import deque
from threading import Thread
from threading import Condition
import time


QUEUE = deque()
CV = Condition()


def _consume():
    while True:
        with CV:
            CV.wait_for(_are_tasks)
            print('have', _get_task())


def _are_tasks():
    return bool(QUEUE)


def _get_task():
    return QUEUE.popleft()


def add_task():
    with CV:
        QUEUE.append(item)
        CV.notify()


def start_worker():
    thread = Thread(target=_consume)
    thread.start()
