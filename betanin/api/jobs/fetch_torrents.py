from betanin.api import events
from betanin.api import process_queue
from betanin.api import status
from betanin.api import torrent_client
from betanin.api.orm.models.torrent import Torrent
from betanin.api.status import BetaStatus
from betanin.api.status import RemoteStatus
from betanin.api.torrent_client import get_torrents
from betanin.extensions import db
from betanin.extensions import scheduler


def _update_basics(torrent, torrent_dict):
    for key, value in torrent_dict.items():
        setattr(torrent, key, value)


def _process(torrent):
    if torrent.has_status(RemoteStatus.DOWNLOADING) \
            and torrent.has_status(BetaStatus.UNKNOWN):
        # will process
        torrent.set_status(BetaStatus.WAITING)
    elif torrent.has_status(RemoteStatus.COMPLETED) \
            and torrent.has_status(BetaStatus.WAITING):
        # process
        process_queue.add(torrent.id)
        torrent.set_status(BetaStatus.ENQUEUED)
        # new status will be set after process
    elif torrent.has_status(RemoteStatus.COMPLETED) \
           and torrent.has_status(BetaStatus.UNKNOWN):
        # won't process
       torrent.set_status(BetaStatus.IGNORED,
           'the torrent finished before betanin saw it')


def _start():
    'fetch torrents from all the remotes, and add them to the db'
    try:
        torrent_groups = list(get_torrents())
    except Exception as exc:
        print(f'problem with remote: {exc}')
        return
    status.clear()
    for torrent_dict in torrent_groups:
        torrent_id = torrent_dict['id']
        torrent = Torrent.get_or_create(torrent_id)
        # update info from the wrapper
        _update_basics(torrent, torrent_dict)
        # add to queue if should
        # (queue worker will update beta status
        _process(torrent)
        # update status for fetch
        status.inc_enum_key(torrent.beta_status)
        # commit
        db.session.add(torrent)
        db.session.commit()
    # tell client to get the latest torrent list
    events.torrents_grabbed()

def start():
    with scheduler.app.app_context():
        _start()
