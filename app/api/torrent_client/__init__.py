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


@dataclass
class Torrent:
    id: str
    name: str
    path: str
    progress: int
    status: object

    def __repr__(self):
        return f'Torrent(id={self.id})'

    @property
    def is_downloaded(self):
        return self.status == RemoteStatus.COMPLETED
