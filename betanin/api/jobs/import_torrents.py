# python
import os.path
from collections import defaultdict

# 3rd party
import gevent
import pexpect
from gevent.queue import Queue

# betanin
from betanin.api import events
from betanin.api.status import Status
from betanin.extensions import db
from betanin.api.orm.models.torrent import Torrent

PROCESSES = {}
INDEXES = {}
QUEUE = Queue()
NEEDS_INPUT_SNIPPETS = (
    '[A]pply',
    'kip new, ',
    'ter search, ente',
    'it, edit ',
)


def _set_init_index(torrent):
    if not torrent.id in INDEXES:
        INDEXES[torrent.id] = torrent.last_line_index


def _add_line(torrent, data):
    _set_init_index(torrent)
    index = INDEXES[torrent.id]
    INDEXES[torrent.id] += 1
    torrent.add_line(index, data)
    db.session.commit()
    events.send_line_read(torrent.id, index, data)


def _calc_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _read_and_send_pty_out(proc, torrent):
    while True:
        try:
            data = proc.read_nonblocking(1024, 0.05)
        except pexpect.exceptions.TIMEOUT:
            gevent.sleep(1)
            continue
        except pexpect.exceptions.EOF:
            break
        text = data.decode()
        if text.isspace():
            continue
        _add_line(torrent, text)
        if any(match in text for match in NEEDS_INPUT_SNIPPETS):
            torrent.status = Status.NEEDS_INPUT
            db.session.commit()
            events.send_torrents_changed()
            events.send_torrent_status_changed(torrent)


def _import_torrent(torrent):
    proc = pexpect.spawn(
        f'/home/senan/dev/repos/betanin/scripts/mock_beets', use_poll=True)
        # f'beet import -c {_calc_import_path(torrent)!r}', use_poll=True)
    PROCESSES[torrent.id] = proc
    _read_and_send_pty_out(proc, torrent)
    exit_status = _right_exit_status(proc.exitstatus)
    return exit_status


def _right_exit_status(exit_status):
    if exit_status is None:
        return 0
    return exit_status


def send_input(torrent_id, text):
    PROCESSES[torrent_id].sendline(text)


def add(**kwargs):
    torrent = Torrent(**kwargs)
    torrent.status = Status.ENQUEUED
    db.session.add(torrent)
    db.session.commit()
    QUEUE.put_nowait(torrent.id)
    events.send_torrents_changed()


def retry(torrent_id):
    query = Torrent.query.filter_by(id=torrent_id)
    torrent = query.first_or_404()
    torrent.status = Status.ENQUEUED
    db.session.commit()
    _add_line(torrent, '[betanin] retrying...')
    events.send_torrents_changed()
    QUEUE.put_nowait(torrent.id)


def start():
    while True:
        torrent_id = QUEUE.get()
        torrent = Torrent.query.get(torrent_id)
        torrent.status = Status.PROCESSING
        db.session.commit()
        events.send_torrents_changed()
        _add_line(torrent, '[betanin] starting cli program')
        return_code = _import_torrent(torrent)
        _add_line(torrent, '[betanin] program finished with '
            f'exit status `{return_code}`')
        if return_code == 0:
            torrent.status = Status.COMPLETED
        else:
            torrent.status = Status.FAILED
        db.session.commit()
        events.send_torrents_changed()
        events.send_torrent_status_changed(torrent)
