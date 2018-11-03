# python
import os.path
import subprocess

# 3rd party
import gevent
from gevent.queue import Queue

# betanin
from betanin.api import events
from betanin.api.status import Status
from betanin.extensions import db
from betanin.api.orm.models.torrent import Torrent

PROCESSES = {}
QUEUE = Queue()


def _add_line(torrent, index, data):
    torrent.add_line(index, data)
    db.session.commit()
    events.line_read(torrent.id, index, data)


def _calc_import_path(torrent):
    return os.path.join(torrent.path, torrent.name)


def _import_torrent(torrent):
    torrent.delete_lines()
    _add_line(torrent, -1, '[betanin] starting cli program')
    proc = subprocess.Popen(
        ['beet', 'import', '-c', _calc_import_path(torrent)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1,
    )
    PROCESSES[torrent.id] = proc
    for i, raw_line in enumerate(iter(proc.stdout.readline, '')):
        # TODO: add regex here to update status to
        # possibly update NEEDS_INPUT
        data = raw_line.rstrip()
        _add_line(torrent, i, data)
    proc.stdout.close()
    proc.wait()
    return_code = proc.returncode
    _add_line(torrent, 2**22, '[betanin] program finished with '
        f'exit status `{return_code}`')
    return return_code


def add(**kwargs):
    torrent = Torrent(**kwargs)
    torrent.status = Status.ENQUEUED
    # add and commit the new torrent because the queue
    # and socket/ajax event will need them to be
    db.session.add(torrent)
    db.session.commit()
    # add to queue
    QUEUE.put_nowait(torrent.id)
    # tell client to get latest torrents
    events.torrents_changed()


def remove(**kwargs):
    torrent = Torrent(**kwargs)
    # dont store lines that dont have an associated torrent
    db.session.execute(
        'DELETE FROM lines WHERE id = :id',
        {'id': torrent.id})
    # delete the actual torrent second in case of foreign key
    db.session.execute(
        'DELETE FROM torrents WHERE id = :id',
        {'id': torrent.id})
    db.session.commit()
    # send a howdy to the client
    events.torrents_changed()


def start():
    while True:
        torrent_id = QUEUE.get()
        torrent = Torrent.query.get(torrent_id)
        torrent.status = Status.PROCESSING
        db.session.commit()
        events.torrents_changed()
        return_code = _import_torrent(torrent)
        if return_code == 0:
            torrent.status = Status.COMPLETED
        else:
            torrent.status = Status.FAILED
        db.session.commit()
        events.torrents_changed()
