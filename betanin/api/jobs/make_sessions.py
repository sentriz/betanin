from betanin.api import torrent_client
from betanin.extensions import scheduler

def start():
    with scheduler.app.app_context():
        print('starting job make sessions')
        torrent_client.make_sessions()
        print('finished, sessions are', torrent_client.SESSIONS)

