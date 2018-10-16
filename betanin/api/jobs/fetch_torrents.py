from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.api import torrent_client
from betanin.extensions import db
from betanin.extensions import scheduler
from betanin.api.status import RemoteStatus
from betanin.api.status import BetaStatus
from betanin.api import status
from betanin.api.jobs import process_torrents
from betanin.api.torrent_client import get_torrents


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
        process_torrents.add(torrent.id)
        torrent.set_status(BetaStatus.ENQUEUED)
        # new status will be set after process
    elif torrent.has_status(RemoteStatus.COMPLETED) \
           and torrent.has_status(BetaStatus.UNKNOWN):
        # won't process
       torrent.set_status(BetaStatus.IGNORED,
           'the torrent finished before betanin saw it')
    else:
        to_ignore = (
            (RemoteStatus.DOWNLOADING, BetaStatus.WAITING),
            (RemoteStatus.COMPLETED,   BetaStatus.IGNORED),
            (RemoteStatus.COMPLETED,   BetaStatus.ENQUEUED),
            (RemoteStatus.COMPLETED,   BetaStatus.PROCESSING),
            (RemoteStatus.COMPLETED,   BetaStatus.COMPLETED),
        )
        for r_s, b_s in to_ignore:
            if torrent.remote_status == r_s and \
                    torrent.beta_status == b_s:
                break
        else:
            raise UserWarning(f'not sure how to handle {torrent}')

def start():
    'fetch torrents from all the remotes, and add them to the db'
    with scheduler.app.app_context():
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
