import pickle
from app.api import paths 
import os


def _write_pickle(torrents, pickle_path=paths.PICKLE_PATH):
    with open(pickle_path, 'wb') as handle:
        return pickle.dump(torrents, handle, protocol=pickle.HIGHEST_PROTOCOL)


def _read_pickle(pickle_path=paths.PICKLE_PATH):
    if not os.path.isfile(pickle_path):
        return set()
    with open(pickle_path, 'rb') as handle:
        return pickle.load(handle)


def see(torrent_id):
    hashes = _read_pickle()
    hashes.add(torrent_id)
    _write_pickle(hashes)


def forget(torrent_id):
    hashes = _read_pickle()
    hashes.remove(torrent_id)
    _write_pickle(hashes)


def was_seen(torrent_id):
    return torrent_id in _read_pickle()
