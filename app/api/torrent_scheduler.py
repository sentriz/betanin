import time
from threading import Thread

from app import api
from app.api import torrent_client
from app.api import state
from app.api import beet_queue

import requests


INTERVAL = 5


def _process(torrent):
    if torrent.is_downloaded:
        if state.was_seen(torrent.id):
            beet_queue.add_task(torrent)
            state.forget(torrent.id)
    else:
        state.see(torrent.id)


def _worker():
    print("starting torrent worker")
    while True:
        api.torrents = list(torrent_client.get_torrents())
        for torrent in api.torrents:
            _process(torrent)
        time.sleep(INTERVAL)


def start_worker():
    thread = Thread(target=_worker)
    thread.start()
