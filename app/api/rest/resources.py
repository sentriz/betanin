from datetime import datetime

from flask import request
from flask_restplus import Api
from transmission import Transmission

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest
import app.config_transmission as trans_config

def filter_torrents_in(torrents):
    for torrent in torrents:
        if torrent['downloadDir'] != trans_config.DIRECTORY:
            continue
        yield torrent 


def clean_torrents_out(torrents):
    for torrent in torrents:
        del torrent['downloadDir']
        torrent['percentDone'] *= 100
        torrent['isFinished'] = torrent['percentDone'] == 100
        torrent['startDate'] = torrent['startDate'].isoformat()
        yield torrent


@api_rest.route('/transmission')
class TransmissionResource(BaseResource):
    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
        self.session = Transmission(
            host=trans_config.HOST,
            port=trans_config.PORT,
            username=trans_config.USERNAME,
            password=trans_config.PASSWORD,
            ssl=trans_config.SSL,
        )

    def get(self):
        all_torrents = self.session('torrent-get',
                                    fields=[
                                        'name',
                                        'downloadDir', 
                                        'isFinished',
                                        'id',
                                        'percentDone',
                                        'startDate',
                                    ])
        music_torrents = filter_torrents_in(all_torrents['torrents'])
        response = clean_torrents_out(music_torrents)
        return list(response)

    def post(self):
        json_payload = request.json
        return {'timestamp': json_payload}, 201

