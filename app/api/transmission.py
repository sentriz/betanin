from datetime import datetime

from flask import request
from flask_restplus import Api
from transmission import Transmission

from app.api import api_rest
from app.api import state
from app.api.paths import config
# from app.api.paths import read_pickle
from app.api.rest.base import BaseResource
from app.api.rest.base import SecureResource


_session = Transmission(
    host=config.TRANSMISSION['host'],
    port=config.TRANSMISSION['port'],
    username=config.TRANSMISSION['username'],
    password=config.TRANSMISSION['password'],
    ssl=config.TRANSMISSION['ssl'],
)

def torrent_is_done(torrent):
    return torrent['leftUntilDone'] == 0


def filter_torrents_in(torrents):
    for torrent in torrents:
        if torrent['downloadDir'] != config.DIRECTORY:
            continue
        torrent_id = torrent['hashString']
        if torrent_is_done(torrent):
            if state.was_seen(torrent_id):
                print("process_torrent(torrent)")
                state.forget(torrent_id)
            continue
        else:
            state.see(torrent_id)
        yield torrent 


def clean_torrents_out(torrents):
    for torrent in torrents:
        del torrent['downloadDir']
        torrent['percentDone'] *= 100
        torrent['isFinished'] = torrent['percentDone'] == 100
        torrent['startDate'] = torrent['startDate'].isoformat()
        yield torrent


def get_torrents():
    all_torrents = _session('torrent-get',
                            fields=[
                                'name',
                                'downloadDir', 
                                'isFinished',
                                'id',
                                'hashString',
                                'percentDone',
                                'startDate',
                                'leftUntilDone',
                            ])
    music_torrents = list(filter_torrents_in(all_torrents['torrents']))
    response = list(clean_torrents_out(music_torrents))
    print("STATE IS", state._read_pickle())
    return response
