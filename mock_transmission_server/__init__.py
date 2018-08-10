from flask import Flask
from flask import jsonify
from flask import request
from mock_transmission_server import response
from threading import Thread
import time


app = Flask(__name__)


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


@app.route("/transmission/rpc", methods=['POST'])
def main():
    req = request.get_json(force=True)
    if 'tag' in req:
        print('request had tag', req['tag'])
        response.TAG = req['tag']
    return jsonify(
        arguments=response.ARGUMENTS,
        result=response.RESULT,
        tag=response.TAG,
    )


def _inc_worker(percent, period):
    while True:
        _inc_torrent(percent)
        time.sleep(period)


def start_inc_worker(**kwargs):
    Thread(target=_inc_worker, 
           kwargs=kwargs).start()
