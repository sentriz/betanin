# python
from enum import Enum

# betanin
from betanin.extensions import db

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
        column: count for column, count in results
        if count != 0
    }
