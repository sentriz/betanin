# standard library
import os.path
from collections import defaultdict

# 3rd party
import gevent
import pexpect
from gevent.queue import Queue

# betanin
from betanin.api import events
from betanin.api import notifications
from betanin.api.status import Status
from betanin.extensions import db
from betanin.extensions import socketio
from betanin.api.orm.models.torrent import Line
from betanin.api.orm.models.torrent import Torrent


PROCESSES = {}
QUEUE = Queue()
NEEDS_INPUT_SNIPPETS = (
    '[A]pply',
    'kip new, ',
    'ter search, ente',
    'it, edit ',
)


def _add_line(torrent, data):
    line = Line(data=data)
    torrent.add_line(line)
    db.session.commit()
    events.send_line(line)


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
            events.send_torrent(torrent)
            notifications.send_async(torrent)


def _import_torrent(torrent):
    proc = pexpect.spawn(
        # f'/home/senan/dev/repos/betanin/scripts/mock_beets', use_poll=True)
        f'beet import --copy --noresume {_calc_import_path(torrent)!r}', use_poll=True)
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
    events.send_torrent(torrent)


def retry(torrent_id):
    query = Torrent.query.filter_by(id=torrent_id)
    torrent = query.first_or_404()
    torrent.status = Status.ENQUEUED
    db.session.commit()
    _add_line(torrent, '[betanin] retrying... '
            f'(there are {len(QUEUE)} items in the queue)')
    events.send_torrent(torrent)
    QUEUE.put_nowait(torrent.id)


def _start():
    while True:
        torrent_id = QUEUE.get()
        torrent = Torrent.query.get(torrent_id)
        torrent.status = Status.PROCESSING
        db.session.commit()
        _add_line(torrent, '[betanin] starting cli program')
        events.send_torrent(torrent)
        return_code = _import_torrent(torrent)
        _add_line(torrent, '[betanin] program finished with '
            f'exit status `{return_code}`')
        torrent.status = Status.FAILED
        if return_code == 0:
            torrent.status = Status.COMPLETED
        db.session.commit()
        events.send_torrent(torrent)
        notifications.send_async(torrent)


def start(flask_app):
    def with_context():
        with flask_app.app_context():
            _start()
    return socketio.start_background_task(with_context)
