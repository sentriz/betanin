# standard library
import os

# 3rd party
from loguru import logger

# betanin
from betanin import paths


_LENGTH = 32


def _gen():
    return os.urandom(_LENGTH).hex()


def _file_exists():
    return os.path.exists(paths.SECRET_KEY_PATH)


def _write(key):
    with open(paths.SECRET_KEY_PATH, "w") as file:
        file.write(key)


def read():
    with open(paths.SECRET_KEY_PATH, "r") as file:
        return file.read()


def ensure():
    if not _file_exists():
        _write(_gen())
        logger.info(
            f"secret key `{paths.SECRET_KEY_PATH}`: does not exist - creating"
        )
    else:
        logger.info(f"using secret key `{paths.SECRET_KEY_PATH}`")
