import time
import random

from betanin.api.models.torrent import Torrent
from betanin.extensions import scheduler
from betanin.extensions import db
from flask import current_app


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


def start():
    scheduler.app.app_context().push()
    # db.session.add(Torrent(id=random.randint(20, 400), name="san", path="sam"))
    # db.session.commit()
    print(Torrent.query.all())
