from betanin.api.status import RemoteStatus

from transmission import Transmission
import transmission
import requests
import json


DEFAULT_CONFIG = {
    'path': '/transmission/rpc',
}


def _torrent_raw_to_dict(raw):
    return {
        'remote_status': (RemoteStatus.DOWNLOADING,
                          RemoteStatus.COMPLETED)[raw['leftUntilDone'] == 0],
        'id':            raw['hashString'],
        'progress':      raw['percentDone'] * 100,
        'path':          raw['downloadDir'],
        'name':          raw['name'],
    }


class Client:
    def __init__(self, row):
        self.row = row
        self._session = self._create_session()

    def _create_session(self):
        return Transmission(
            host=self.row.config['hostname'],
            port=int(self.row.config['port']),
            username=self.row.config['username'],
            password=self.row.config['password'],
            ssl=self.row.config['ssl'],
            path=self.row.config['path'],
        )

    def _should_process(self, raw):
        if not self._torrent_is_music(raw):
            return False
        # more
        return True

    def _torrent_is_music(self, raw):
        return raw['downloadDir'] == self.row.config['category']

    def get_torrents(self):
        print(f'fetching torrents from transmission #{self.row.id}')
        raw_torrents = self._session(
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
        yield from (_torrent_raw_to_dict(raw) \
                        for raw in torrents  \
                        if self._should_process(raw))

    def test_connection(self):
        try:
            version = self.session('session-get')['version']
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
