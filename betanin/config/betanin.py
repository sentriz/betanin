# standard library
import os
import sys
from contextlib import contextmanager

# 3rd party
import toml
from loguru import logger

# betanin
from betanin import paths


_API_KEY_LENGTH = 16
_DEFAULT_CONFIG = {
    "frontend": {"username": "", "password": ""},
    "notifications": {
        "services": {},
        "strings": {
            "body": "@ $time. view/use the console at http://127.0.0.1:9393/$console_path",
            "title": "[betanin] torrent `$name` $status",
        },
    },
    "clients": {"api_key": ""},
}
_NEEDED_CONFIG_PATHS = (
    # (path, ) reason
    (("frontend", "username"), "please provide a frontend username"),
    (("frontend", "password"), "please provide a frontend password"),
    (("clients", "api_key"), "please provide a client api key"),
)


def _gen_api_key():
    return os.urandom(_API_KEY_LENGTH).hex()


def _file_exists():
    return os.path.exists(paths.CONFIG_PATH)


def _path_exist(dict_, *path):
    _dict = dict_
    for key in path:
        try:
            _dict = _dict[key]
        except KeyError:
            return False
        else:
            if not _dict:
                return False
    return True


def read():
    with open(paths.CONFIG_PATH, "r") as file:
        return toml.load(file)


def write(config):
    with open(paths.CONFIG_PATH, "w") as file:
        toml.dump(config, file)


@contextmanager
def mutate():
    config = read()
    yield config
    write(config)


def credentials_correct(username, password):
    config = read()
    return (
        username == config["frontend"]["username"]
        and password == config["frontend"]["password"]
    )


def api_key_correct(api_key):
    return api_key == read()["clients"]["api_key"]


def get_api_key():
    return read()["clients"]["api_key"]


def ensure():
    if not _file_exists():
        logger.error(
            f"config `{paths.CONFIG_PATH}`: does not exist - creating and exiting"
        )
        _DEFAULT_CONFIG["clients"]["api_key"] = _gen_api_key()
        write(_DEFAULT_CONFIG)
        sys.exit(1)
    else:
        config = read()
        for path, reason in _NEEDED_CONFIG_PATHS:
            if _path_exist(config, *path):
                continue
            logger.error(f"config `{paths.CONFIG_PATH}`: {reason}")
            sys.exit(1)
    logger.info(f"using config `{paths.CONFIG_PATH}`")
