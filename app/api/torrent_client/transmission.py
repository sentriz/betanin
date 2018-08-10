from datetime import datetime

from flask import request
from flask_restplus import Api
from transmission import Transmission

from app import bet_config
from app.api import torrent_client 


_session = Transmission(
    host=bet_config.TRANSMISSION['host'],
    port=bet_config.TRANSMISSION['port'],
    username=bet_config.TRANSMISSION['username'],
    password=bet_config.TRANSMISSION['password'],
    ssl=bet_config.TRANSMISSION['ssl'],
)


def _torrent_is_done(torrent):
    return torrent['leftUntilDone'] == 0


def _torrent_is_music(torrent):
    return torrent['downloadDir'] == bet_config.DIRECTORY


def _torrent_status_to_object(torrent):
    if _torrent_is_done(torrent):
        return torrent_client.RemoteStatus.COMPLETED
    else:
        return torrent_client.RemoteStatus.DOWNLOADING


def _torrent_to_object(torrent):
    return {
        'remote_status': _torrent_status_to_object(torrent),
        'id':            torrent['hashString'],
        'progress':      torrent['percentDone'] * 100,
        'path':          torrent['downloadDir'],
        'name':          torrent['name'],
        'done_date':     torrent['doneDate']
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
