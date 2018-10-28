from enum import Enum
from collections import defaultdict
from betanin.extensions import db



torrent_count = 0
Status = Enum('Status', [
    'COMPLETED',
    'ENQUEUED',
    'FAILED',
    'IGNORED',
    'NEEDS_INPUT',
    'PROCESSING',
])


def fetch():
    prox = db.session.execute(
        'SELECT status, count() FROM torrents GROUP BY status;'
    )
    results = prox.fetchall()
    return {
        **{column: count for column, count in
            results if count != 0},
        'TOTAL': torrent_count,
    }
