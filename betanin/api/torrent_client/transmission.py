from betanin.api import status

from transmission import Transmission
import requests
import json


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


DEFAULT_CONFIG = {
    'host': None,
    'port': None,
    'username': None,
    'password': None,
    'path': '/transmission/rpc',
    'ssl': False,
}


def create_session(config):
    return Transmission(
        host=config['hostname'],
        port=int(config['port']),
        username=config['username'],
        password=config['password'],
        ssl=config['ssl'],
        path=config['path'],
    )


def test_connection(session):
    try:
        version = session('session-get')['version']
        return True, f'connected to transmission {version}'
    except (requests.exceptions.ConnectionError, 
            requests.exceptions.InvalidURL):
        return False, f'invaid hostname/port/ssl'
    except json.decoder.JSONDecodeError:
        return False, f'invalid response from host'


def get_torrents(session):
    print('fetching torrents from client')
    raw_torrents = session(
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
