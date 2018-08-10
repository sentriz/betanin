from dataclasses import dataclass
from enum import Enum
import importlib


# TODO: not have Status and Torrent in here


_remote = 'transmission'
# TODO: not this
get_torrents = importlib.import_module('app.api.torrent_client.' + _remote).get_torrents


RemoteStatus = Enum('RemoteStatus', [
    'COMPLETED', 
    'DOWNLOADING',
    'INACTIVE',
])

BetaStatus = Enum('BetaStatus', [
    'ENQUEUED',
    'PROCESSING',
    'NEEDS_INPUT',
    'FAILED',
    'COMPLETED', 
])
