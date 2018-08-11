import time

from betanin import context
from betanin.api import torrent_client
from betanin.api import beet_queue
from betanin.api import events

import requests
import gevent


INTERVAL = 2


def _process(torrent):
    pass
    # # 'torrent seen' -> on the last iteration, the torrent was downloading
    # # and betanin indented to process it when it finishes 
    # if not state.was_seen(torrent.id) and torrent.is_downloaded:
    #     return
    # # torrent is new and (downloading or downloaded)
    # if torrent.is_downloaded:
    #     beet_queue.add(torrent)
    #     state.mark_imported(torrent.id)
    # else: # torrent is downloading
    #     state.is_downloading(torrent.id)


def _update_torrents():
    print(context.db)
    new_torrents = list(torrent_client.get_torrents())


def _worker():
    while True:
        _update_torrents()
        # for key, value in list(torrent_client.get_torrents())
            
        # for torrent in api.torrents:
        #     _process(torrent)
        # events.torrents_grabbed()
        gevent.sleep(INTERVAL)


def start_worker():
    print("starting client worker")
    gevent.spawn(_worker)
