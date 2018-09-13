from betanin.config.client import get_or_set_default
from betanin.api import status

from transmission import Transmission


print('__name__ is', __name__)

CONFIG = get_or_set_default('transmission', {
    'host': '',
    'port': 0,
    'username': '',
    'password': '',
    'ssl': False,
})


def _torrent_is_done(torrent):
    return torrent['leftUntilDone'] == 0


def _torrent_is_music(torrent):
    return torrent['downloadDir'] == client.DIRECTORY


def _torrent_status_to_object(torrent):
    if _torrent_is_done(torrent):
        return status.RemoteStatus.COMPLETED
    else:
        return status.RemoteStatus.DOWNLOADING


def _torrent_to_object(torrent):
    return {
        'remote_status': _torrent_status_to_object(torrent),
        'id':            torrent['hashString'],
        'progress':      torrent['percentDone'] * 100,
        'path':          torrent['downloadDir'],
        'name':          torrent['name'],
    }


def _should_process(torrent):
    if not _torrent_is_music(torrent):
        return False
    # more
    return True


def get_torrents():
    print('fetching torrents from client')
    raw_torrents = _session(
        'torrent-get',
        fields=[
            'name',
            'downloadDir',
            'isFinished',
            'hashString',
            'percentDone',
            'startDate',
            'leftUntilDone',
        ]
    )
    torrents = raw_torrents['torrents']
    yield from map(_torrent_to_object,
                   filter(_should_process, torrents))
