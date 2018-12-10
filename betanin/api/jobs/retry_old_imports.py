# betanin
from betanin.api.status import Status
from betanin.api.orm.models.torrent import Torrent
from betanin.api.jobs.import_torrents import retry


def _start():
    old_imports = Torrent.query.filter(
        (Torrent.status == Status.ENQUEUED) | \
        (Torrent.status == Status.PROCESSING) | \
        (Torrent.status == Status.NEEDS_INPUT)
    )
    for torrent in old_imports.all():
        retry(torrent.id)


def start(flask_app):
    with flask_app.app_context():
        _start()
