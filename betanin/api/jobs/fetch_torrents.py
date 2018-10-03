from betanin.api import events
from betanin.api.orm.models.torrent import Torrent
from betanin.api import torrent_client
from betanin.extensions import db
from betanin.extensions import scheduler
from betanin.api.status import RemoteStatus
from betanin.api.status import BetaStatus
from betanin.api.jobs import process_torrents
from betanin.api.torrent_client import get_torrents


def _update_basics(torrent, torrent_dict):
    for key, value in torrent_dict.items():
        setattr(torrent, key, value)


def _process(torrent):
    if torrent.remote_status == RemoteStatus.DOWNLOADING:
        torrent.set_beta_status('waiting')
        torrent.should_process = True
        return
    if torrent.remote_status == RemoteStatus.COMPLETED \
            and torrent.should_process:
        # sets extra remote_status
        print('+++ adding', torrent)
        torrent.should_process = False
        process_torrents.add(torrent.id)
        torrent.set_beta_status('enqueued')
        return
    if torrent.beta_status == BetaStatus.UNKNOWN:
        torrent.set_beta_status('ignored',
            'the torrent existed before betanin did')


def start():
    with scheduler.app.app_context():
        try:
            torrents = list(get_torrents())
            print('torrents are', torrents)
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
            db.session.add(torrent)
            _process(torrent)
        # tell client to get the latest torrent list
        db.session.commit()
        events.torrents_grabbed()
