from enum import Enum
from collections import defaultdict
from betanin.extensions import db



torrent_count = 0
Status = Enum('Status', [
    'DOWNLOADING',
    'DOWNLOADED',
    'ENQUEUED',
    'PROCESSING',
    'NEEDS_INPUT',
    'FAILED',
    'PROCESSED',
    'IGNORED',
])


def fetch():
    prox = db.session.execute('SELECT status, COUNT(status) from torrents;')
    return {
        **dict(prox.fetchall()),
        'TOTAL': torrent_count
    }
