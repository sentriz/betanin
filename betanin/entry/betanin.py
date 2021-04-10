# doing this ugly import thing seems to be the
# only thing i can do where isort/autoflake8/black don't
# freak out
gevent = __import__("gevent.monkey")
gevent.monkey.patch_all()

# standard library
import sys
import signal

# 3rd party
import click
import gevent
from loguru import logger

# betanin
import betanin.config.betanin as conf_betanin
import betanin.config.secret_key as conf_secret_key
from betanin import application
from betanin import system_info
from betanin.jobs import serve_web
from betanin.jobs import import_torrents
from betanin.jobs import migrate_database
from betanin.jobs import retry_old_imports
from betanin.jobs import register_notifications


def _print_meta_info():
    for name, value in system_info.SYSTEM_INFO.items():
        logger.info(f"{name} - {value}")


def _stop(sig_num, frame):
    logger.info("shutting down")
    sys.exit()


def _make_starter(flask_app, module, *args, **kwargs):
    logger.info(f"starting job {module.__name__}")
    return module.start(flask_app, *args, **kwargs)


@click.command()
@click.option(
    "--host",
    default="",
    envvar="BETANIN_HOST",
    help="the host to bind to for webui/api/hook",
)
@click.option(
    "--port",
    default=9393,
    envvar="BETANIN_PORT",
    help="the port to listen on for webui/api/hook",
)
def main(host, port):
    "starts betanin"
    _print_meta_info()
    # ensure config exists and is valid
    conf_betanin.ensure()
    conf_secret_key.ensure()
    # setup stop
    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)
    # setup start
    gevent.hub.Hub.NOT_ERROR = (OSError, SystemExit)
    flask_app = application.create()
    start_job = lambda module, *args, **kwargs: _make_starter(
        flask_app, module, *args, **kwargs
    )
    # start sync jobs
    start_job(migrate_database)
    start_job(retry_old_imports)
    # start async jobs
    gevent.joinall(
        (
            start_job(register_notifications),
            start_job(serve_web, host, port),
            start_job(import_torrents),
        )
    )


if __name__ == "__main__":
    main(None, None)
