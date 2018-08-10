import time

from app import api
from app.api import torrent_client
from app.api import state
from app.api import beet_queue
from app.api import events

import requests
import eventlet


INTERVAL = 5


def _process(torrent):
    if torrent.is_downloaded:
        if state.was_seen(torrent.id):
            beet_queue.add_torrent(torrent)
            state.forget(torrent.id)
    else:
        state.see(torrent.id)


def _worker():
    while True:
        api.torrents = list(torrent_client.get_torrents())
        for torrent in api.torrents:
            _process(torrent)
        events.torrents_grabbed()
        eventlet.sleep(INTERVAL)


def start_worker():
    print("starting client worker")
    eventlet.spawn(_worker)
