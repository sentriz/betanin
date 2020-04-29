# betanin
from betanin.models import Torrent
from betanin.status import Status
from betanin.jobs.import_torrents import retry


def _start():
    old_imports = Torrent.query.filter(
        (Torrent.status == Status.ENQUEUED)
        | (Torrent.status == Status.PROCESSING)
        | (Torrent.status == Status.NEEDS_INPUT)
    )
    for torrent in old_imports.all():
        retry(torrent.id)


def start(flask_app):
    with flask_app.app_context():
        _start()
