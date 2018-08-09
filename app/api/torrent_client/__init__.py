from dataclasses import dataclass
from enum import Enum
import importlib


_remote = 'transmission'
# TODO: not this
get_torrents = importlib.import_module('app.api.torrent_client.' + _remote).get_torrents


Status = Enum('TorrentStatus', [
    'REMOTE_COMPLETED', 
    'REMOTE_DOWNLOADING',
    'REMOTE_INACTIVE',
    'COMPLETED', 
    'FAILED',
    'NEEDS_INPUT',
    'PROCESSING',
])


@dataclass
class Torrent:
    id: str
    name: str
    path: str
    progress: int
    status: Status

    @property
    def is_downloaded(self):
        return self.status == Status.REMOTE_COMPLETED

    def __repr__(self):
        return f'Torrent(id={self.id})'
