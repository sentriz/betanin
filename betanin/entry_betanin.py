# standard library
import sys
import signal

# 3rd party
import click
import gevent
from loguru import logger

# betanin
from betanin import secret_key
from betanin import application
from betanin import main_config
from betanin import system_info
from betanin.jobs import serve_web
from betanin.jobs import import_torrents
from betanin.jobs import migrate_database
from betanin.jobs import retry_old_imports
from betanin.jobs import register_notifications


def _print_meta_info():
    for name, value in system_info.SYSTEM_INFO.items():
        logger.info(f'{name} - {value}')


def _stop(sig_num, frame):
    logger.info('shutting down')
    sys.exit(0)


def _make_starter(flask_app, module, *args, **kwargs):
    logger.info(f'starting job {module.__name__}')
    return module.start(flask_app, *args, **kwargs)


@click.command()
@click.option(
    '--port',
    default=9393,
    envvar='BETANIN_PORT',
    help='the port to listen on for webui/api/hook',
)
def main(port):
    'starts betanin'
    _print_meta_info()
    # ensure config exists and is valid
    main_config.ensure()
    secret_key.ensure()
    # setup stop
    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)
    # setup start
    flask_app=application.create()
    def start(module, *args, **kwargs):
        return _make_starter(flask_app, module, *args, **kwargs)
    # start sync jobs
    start(migrate_database)
    start(retry_old_imports)
    # start async jobs
    gevent.joinall((
        start(register_notifications),
        start(import_torrents),
        start(serve_web, port),
    ))


if __name__ == '__main__':
    main()
