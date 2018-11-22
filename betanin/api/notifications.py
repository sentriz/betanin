#!/usr/bin/env python3

# python
import configparser
from string import Template

# 3rd party
import apprise

# betanin
from betanin import paths
from betanin.api.status import Status

CONFIG = configparser.ConfigParser()
APPRISE = apprise.Apprise()
TEMPLATES = {}
STATUS_LONG = {
    Status.COMPLETED: 'has completed',
    Status.NEEDS_INPUT: 'needs input',
}


def _service_name(long_name):
    return long_name.partition('_')[-1]


def _read_config():
    CONFIG.read(paths.NOTIFICATION_CONFIG_PATH)
    TEMPLATES['title'] = Template(CONFIG['general']['title'])
    TEMPLATES['body'] = Template(CONFIG['general']['body'])


def _write_config():
    with open(paths.NOTIFICATION_CONFIG_PATH, 'w') as file:
        CONFIG.write(file)


def _string_to_bool(string):
    return string.lower() in ("yes", "true", "t", "1")


def register_all():
    _read_config()
    for name, items in CONFIG.items():
        if not name.startswith('service_'):
            continue
        if not _string_to_bool(items['enabled']):
            continue
        APPRISE.add(items['url'])
        print(f'added notification {name}')


def send(torrent):
    variables = {
        'name': torrent.name,
        'id': torrent.id,
        'time': torrent.updated,
        'status': STATUS_LONG.get(
            torrent.status, str(torrent.status)),
    }
    APPRISE.notify(
        title=TEMPLATES['title'].safe_substitute(variables),
        body=TEMPLATES['body'].safe_substitute(variables),
    )
