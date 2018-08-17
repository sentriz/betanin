import time
import random

from betanin.api import events
from betanin.api.models.torrent import Torrent
from betanin.api.torrent_client import get_torrents
from betanin.extensions import db
from betanin.extensions import scheduler
from betanin.api.status import RemoteStatus
from betanin.api.status import BetaStatus
from betanin.api.jobs import process_torrents


def _update_basics(torrent, torrent_dict):
    for key, value in torrent_dict.items():
        setattr(torrent, key, value)


def _process(torrent):
    if torrent.remote_status == RemoteStatus.DOWNLOADING:
        torrent.beta_status = BetaStatus.WAITING
        torrent.should_process = True
        return
    if torrent.remote_status == RemoteStatus.COMPLETED \
            and torrent.should_process:
        # sets extra remote_status 
        print("+++ adding", torrent)
        torrent.should_process = False
        process_torrents.add(torrent.id)
        torrent.beta_status = BetaStatus.ENQUEUED
        return
    if torrent.beta_status == BetaStatus.UNKNOWN:
        torrent.beta_status = BetaStatus.IGNORED


def start():
    scheduler.app.app_context().push()
    try:
        torrents = list(get_torrents())
    except Exception as exc:
        print(f'problem with remote: {exc}')
        return
    for torrent_dict in torrents:
        torrent_id = torrent_dict['id']
        torrent = Torrent.get_or_create(torrent_id)
        # update info from the remote
        _update_basics(torrent, torrent_dict)
        # add to queue if should
        # (queue worker will update beta status
        _process(torrent)
        db.session.add(torrent)
    # tell client to get the latest torrent list
    events.torrents_grabbed()
