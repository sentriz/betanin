# standard library
import os.path

# 3rd party
import gevent
from loguru import logger
from ptyprocess import PtyProcessUnicode
from gevent.queue import Queue

# betanin
from betanin import events
from betanin import notifications
from betanin.models import Line
from betanin.models import Torrent
from betanin.status import Status
from betanin.extensions import DB


PROCESSES = {}
QUEUE = Queue()
NEEDS_INPUT_SNIPPETS = (
    "[A]pply",
    "kip new, ",
    "ter search, ente",
    "it, edit ",
)


def _add_line(torrent, data):
    line = Line(data=data)
    torrent.add_line(line)
    DB.session.commit()
    events.send_line(line)


def _calculate_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _read_and_send_pty_out(proc, torrent):
    while True:
        try:
            data = gevent.os.tp_read(proc.fd, 65536)
        except OSError:
            break
        text = data.decode()
        if text.isspace():
            continue
        _add_line(torrent, text)
        if any(match in text for match in NEEDS_INPUT_SNIPPETS):
            torrent.status = Status.NEEDS_INPUT
            DB.session.commit()
            events.send_torrent(torrent)
            notifications.send_async(torrent)


def _import_torrent(torrent):
    proc = PtyProcessUnicode.spawn(
        [
            "beet",
            "import",
            "--noresume",
            _calculate_import_path(torrent),
        ]
    )
    PROCESSES[torrent.id] = proc
    _read_and_send_pty_out(proc, torrent)
    exit_status = _right_exit_status(proc.exitstatus)
    return exit_status


def _right_exit_status(exit_status):
    if exit_status is None:
        return 0
    return exit_status


def send_input(torrent_id, text):
    PROCESSES[torrent_id].write(f"{text}\n")


def add(**kwargs):
    torrent = Torrent(**kwargs)
    torrent.status = Status.ENQUEUED
    DB.session.add(torrent)
    DB.session.commit()
    QUEUE.put_nowait(torrent.id)
    events.send_torrent(torrent)


def retry(torrent_id):
    query = Torrent.query.filter_by(id=torrent_id)
    torrent = query.first_or_404()
    torrent.status = Status.ENQUEUED
    DB.session.commit()
    _add_line(
        torrent,
        "[betanin] retrying... "
        f"(there are {len(QUEUE)} items in the queue)",
    )
    events.send_torrent(torrent)
    QUEUE.put_nowait(torrent.id)


def _start():
    while True:
        torrent_id = QUEUE.get()
        logger.info(f"got new torrent with id {torrent_id}")
        torrent = Torrent.query.get(torrent_id)
        torrent.status = Status.PROCESSING
        DB.session.commit()
        _add_line(torrent, "[betanin] starting cli program")
        events.send_torrent(torrent)
        return_code = _import_torrent(torrent)
        _add_line(
            torrent,
            f"[betanin] program finished with exit status `{return_code}`",
        )
        torrent.status = Status.FAILED
        if return_code == 0:
            torrent.status = Status.COMPLETED
        logger.info(f"torrent finished with return code {return_code}")
        DB.session.commit()
        events.send_torrent(torrent)
        notifications.send_async(torrent)


def start(flask_app):
    def with_context():
        with flask_app.app_context():
            _start()

    return gevent.spawn(with_context)
