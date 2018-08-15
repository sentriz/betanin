from threading import Thread
import time
import os

from utilities.mock_transmission_server import response

from flask import Flask
from flask import jsonify
from flask import request


def _inc_torrent(amount):
    for torrent in response.ARGUMENTS['torrents']:
        if not ('__moving' in torrent and torrent['__moving']):
            continue
        torrent['percentDone'] += amount/100 # +amount%
        torrent['leftUntilDone'] -= amount
        if torrent['percentDone'] > 1:
            torrent['percentDone'] = 1
        if torrent['leftUntilDone'] < 0:
            torrent['leftUntilDone'] = 0
        print(f'torrent is {torrent["percentDone"]} done')
        print(f'torrent is {torrent["leftUntilDone"]} left')


def _main_view():
    req = request.get_json(force=True)
    if 'tag' in req:
        print('request had tag', req['tag'])
        response.TAG = req['tag']
    return jsonify(
        arguments=response.ARGUMENTS,
        result=response.RESULT,
        tag=response.TAG,
    )


def _inc_worker(amount, period):
    while True:
        _inc_torrent(amount)
        time.sleep(period)


def start_inc_worker(**kwargs):
    Thread(target=_inc_worker, 
           kwargs=kwargs).start()


def create_app():
    app = Flask(__name__)
    app.add_url_rule(
        '/transmission/rpc',
        '_main_view',
        _main_view,
        methods=['POST']
    )
    start_inc_worker(
        amount=int(os.environ.get("MOCK_TRANS_AMOUNT", 2)),
        period=int(os.environ.get("MOCK_TRANS_PERIOD", 100)),
    )
    return app
