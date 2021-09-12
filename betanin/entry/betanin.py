# doing this ugly import thing seems to be the
# only thing i can do where isort/autoflake8/black don't
# freak out
gevent = __import__("gevent.monkey")
gevent.monkey.patch_all()

# standard library
import os
import sys
import signal

# 3rd party
import click
import gevent
from loguru import logger
from flask_migrate import upgrade

# betanin
import betanin.config.betanin as conf_betanin
import betanin.config.secret_key as conf_secret_key
from betanin import paths
from betanin import application
from betanin import system_info
from betanin import notifications
from betanin.jobs import serve_web
from betanin.jobs import import_torrents
from betanin.models import Torrent
from betanin.status import Status
from betanin.jobs.import_torrents import retry


def _print_meta_info():
    for name, value in system_info.SYSTEM_INFO.items():
        logger.info(f"{name} - {value}")


def _stop(sig_num, frame):
    logger.info("shutting down")
    sys.exit()


def _retry_old_imports():
    old_imports = Torrent.query.filter(
        (Torrent.status == Status.ENQUEUED)
        | (Torrent.status == Status.PROCESSING)
        | (Torrent.status == Status.NEEDS_INPUT)
    )
    for torrent in old_imports.all():
        retry(torrent.id)


def _migrate_database():
    upgrade(directory=paths.MIGRATIONS_DIR)


def _register_notifications():
    notifications.register_all()


def _ensure_config():
    logger.info(f"using config `{paths.CONFIG_PATH}`")
    if os.path.exists(paths.CONFIG_PATH):
        conf = conf_betanin.read()
        if (
            not conf["frontend"]
            or not conf["frontend"]["username"]
            or not conf["frontend"]["password"]
        ):
            logger.error("please provide a frontend username and password")
            sys.exit(1)
        if not conf["clients"] or not conf["clients"]["api_key"]:
            logger.error("please provide an api key")
            sys.exit(1)
        return
    logger.error(f"`{paths.CONFIG_PATH}`: doesn't exist. creating and exiting")
    conf = conf_betanin.DEFAULT_CONFIG
    conf["clients"]["api_key"] = conf_betanin.gen_api_key()
    conf_betanin.write(conf)
    sys.exit(1)


def _ensure_secret_key():
    logger.info(f"using secret key `{paths.SECRET_KEY_PATH}`")
    if os.path.exists(paths.SECRET_KEY_PATH):
        return
    logger.info(f"`{paths.SECRET_KEY_PATH}`: doesn't exist. creating")
    conf_secret_key.write(conf_secret_key.gen())


def _start_job(flask_app, module, *args, **kwargs):
    logger.info(f"starting job {module.__name__} {args}")
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
    _ensure_config()
    _ensure_secret_key()

    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)

    gevent.hub.Hub.NOT_ERROR = (OSError, SystemExit)

    app = application.create()
    with app.app_context():
        _migrate_database()
        _retry_old_imports()
        _register_notifications()

    conf = conf_betanin.read()
    num_imports = conf_betanin.find_num_parallel_jobs(conf)
    gevent.joinall(
        (
            *(_start_job(app, import_torrents) for _ in range(num_imports)),
            _start_job(app, serve_web, host, port),
        )
    )


if __name__ == "__main__":
    main(None, None)
