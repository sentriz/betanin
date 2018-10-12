from betanin.api import status

from transmission import Transmission
import transmission
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
    'path': '/transmission/rpc',
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
    except transmission.Unauthorized:
        return False, 'invalid username/password'
    except json.decoder.JSONDecodeError:
        return False, 'invalid response from host'
    except (requests.exceptions.ConnectionError,
            requests.exceptions.InvalidURL,
            TimeoutError):
        return False, 'invaid hostname/port/ssl'
    except requests.exceptions.RequestException:
        return False, 'unknown requests problem'


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
