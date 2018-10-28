import gevent

from betanin.api import events
from betanin.api import status
from betanin.api import status
from betanin.api import torrent_client
from betanin.api.jobs import import_torrents
from betanin.api.orm.models.torrent import Torrent
from betanin.api.orm.models.remote import Remote
from betanin.api.status import Status
from betanin.api.torrent_client import get_torrents
from betanin.extensions import db


_fetched_before = {}


def _remote_fetched(remote_id):
    if remote_id not in _fetched_before:
        _fetched_before[remote_id] = Remote.query.get(remote_id).fetched_before
    else:
        return _fetched_before[remote_id]


def _fetch_one():
    'fetch torrents from all the remotes, and add them to the db'
    try:
        torrent_groups = list(get_torrents())
        status.torrent_count = len(torrent_groups)
    except Exception as exc:
        print(f'problem with remote: {exc}')
        return
    for torrent_dict in torrent_groups:
        if not _remote_fetched(torrent_dict['remote_id']):
            if torrent_dict['status'] == Status.DOWNLOADED:
                # the torrent was downloaded on first fetch, ignore it
                db.session.add(Torrent(
                    id=torrent_dict['id'],
                    status=Status.IGNORED))
            else:
                # the torrent is downloading on first fetch, store it
                db.session.add(Torrent(**torrent_dict))
        elif torrent_dict['status'] == Status.DOWNLOADED:
            # the torrent is downloaded after fetching before, import it
            import_torrents.add(torrent_dict['id'])
    db.session.commit()
    # tell client to get the latest torrent list
    events.torrents_grabbed()


def start():
    while True:
        _fetch_one()
        gevent.sleep(6)
