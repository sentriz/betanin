# standard library
import os

# betanin
from betanin.paths import BEETS_CONFIG_PATH


def get_config():
    if not BEETS_CONFIG_PATH or not os.path.exists(BEETS_CONFIG_PATH):
        return ""
    with open(BEETS_CONFIG_PATH, "r+") as file:
        return file.read()


def set_config(config):
    if not BEETS_CONFIG_PATH:
        return
    with open(BEETS_CONFIG_PATH, "wb") as file:
        file.write(config.encode("utf-8"))


def import_torrent():
    # TODO: move logic from import_torrents to here
    pass
