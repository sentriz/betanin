from datetime import datetime

from flask import request
from flask_restplus import Api
from transmission import Transmission

from app.api.paths import config
from app.api import torrent_client 


_session = Transmission(
    host=config.TRANSMISSION['host'],
    port=config.TRANSMISSION['port'],
    username=config.TRANSMISSION['username'],
    password=config.TRANSMISSION['password'],
    ssl=config.TRANSMISSION['ssl'],
)


def _torrent_is_done(torrent):
    return torrent['leftUntilDone'] == 0


def _torrent_is_music(torrent):
    return torrent['downloadDir'] == config.DIRECTORY


def _torrent_status_to_object(torrent):
    if _torrent_is_done(torrent):
        return torrent_client.Status.REMOTE_COMPLETED
    else:
        return torrent_client.Status.REMOTE_DOWNLOADING


def _torrent_to_object(torrent):
    return torrent_client.Torrent(
        status=_torrent_status_to_object(torrent),
        id=torrent['hashString'],
        progress=torrent['percentDone'] * 100,
        path=torrent['downloadDir'],
        name=torrent['name'],
    )


def _should_process(torrent):
    if not _torrent_is_music(torrent):
        return False
    # more
    return True


def get_torrents():
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
