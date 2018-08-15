import time
import random

from betanin.api.models.torrent import Torrent
from betanin.api.torrent_client import get_torrents
from betanin.extensions import scheduler
from betanin.extensions import db


def _process(torrent):
    return
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


def start():
    scheduler.app.app_context().push()
    for torrent_dict in list(get_torrents()):
        # update remote status
        torrent = Torrent.update_or_create(torrent_dict)
        # update beta status (while processing)
        _process(torrent)
        db.session.add(torrent)
    db.session.commit()
