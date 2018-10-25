import gevent

from betanin.api import events
from betanin.api import status
from betanin.api import status
from betanin.api import torrent_client
from betanin.api.jobs import import_torrents
from betanin.api.orm.models.torrent import Torrent
from betanin.api.status import Status
from betanin.api.torrent_client import get_torrents
from betanin.extensions import db


def fetch_one():
    'fetch torrents from all the remotes, and add them to the db'
    try:
        torrent_groups = list(get_torrents())
        status.torrent_count = len(torrent_groups)
    except Exception as exc:
        print(f'problem with remote: {exc}')
        return
    for torrent_dict in torrent_groups:
        torrent_id = torrent_dict['id']
        if Torrent.exists(torrent_id):
            if torrent_dict['status'] == Status.DOWNLOADED:
                torrent = db.session.query(Torrent).get(torrent_id)
                # add the to the process queue
                import_torrents.add(torrent_id)
        elif torrent_dict['status'] == Status.DOWNLOADING:
            torrent = Torrent(**torrent_dict)
            db.session.add(torrent)
    db.session.commit()
    # tell client to get the latest torrent list
    events.torrents_grabbed()


def start():
    while True:
        fetch_one()
        gevent.sleep(6)
