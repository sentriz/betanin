from betanin.config import client
from betanin.api import status

from transmission import Transmission


_session = Transmission(
    host=client.TRANSMISSION['host'],
    port=client.TRANSMISSION['port'],
    username=client.TRANSMISSION['username'],
    password=client.TRANSMISSION['password'],
    ssl=client.TRANSMISSION['ssl'],
)


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
