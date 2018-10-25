from transmission import Transmission
import json
import os.path
import requests
import transmission
import pickle

from betanin.api.status import Status


DEFAULT_CONFIG = {
    'path': '/transmission/rpc',
}


def _torrent_raw_to_dict(raw):
    return {
        'status': (Status.DOWNLOADING, Status.DOWNLOADED) \
            [raw['leftUntilDone'] == 0],
        'id':       raw['hashString'],
        'progress': raw['percentDone'] * 100,
        'path':     raw['downloadDir'],
        'name':     raw['name'],
    }


class Client:
    def __init__(self, row):
        self.row = row
        self._session = self._create_session()

    def _create_session(self):
        possible_port = self.row.config.get('port')
        if possible_port and possible_port.isdigit():
            possible_port = int(possible_port)
        return Transmission(
            host=self.row.config.get('hostname'),
            port=possible_port,
            username=self.row.config.get('username'),
            password=self.row.config.get('password'),
            ssl=self.row.config.get('ssl'),
            path=self.row.config.get('path'),
        )

    def _should_process(self, raw):
        if not self._torrent_is_music(raw):
            return False
        # more
        return True

    def _torrent_is_music(self, raw):
        return raw['downloadDir'] == self.row.config['category']

    def calc_import_path(self, remote_path, name):
        if 'localDir' in self.row.config:
            return os.path.join(self.row.config['localDir'], name)
        else:
            return os.path.join(remote_path, name)


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
            version = self._session('session-get')['version']
            return True, f'connected to transmission {version}'
        except transmission.Unauthorized:
            return False, 'invalid username/password'
        except (json.decoder.JSONDecodeError,
                KeyError):
            return False, 'invalid response from host'
        except (requests.exceptions.ConnectionError,
                requests.exceptions.InvalidURL,
                TimeoutError):
            return False, 'invaid hostname/port/ssl'
        except requests.exceptions.RequestException:
            return False, 'unknown requests problem'
