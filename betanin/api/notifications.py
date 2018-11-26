#!/usr/bin/env python3

# python
import os
import random
import string
import configparser
from string import Template
from contextlib import contextmanager

# 3rd party
import toml
import apprise

# betanin
from betanin import paths
from betanin.api.status import Status

APPRISE = apprise.Apprise()
STATUS_LONG = {
    Status.COMPLETED: 'has completed',
    Status.NEEDS_INPUT: 'needs input',
}
DEFAULT_CONFIG = {
    'general': {
        'title': '[betanin] torrent `$name` $status',
        'body': '[betanin] torrent `$name` $status, on $time'
    },
    'services': {
        'nvkij8z0hqtgf5f1': {
            'url': 'mailto://one.kelly:kmqkhblhiks@gmail.com?name=one',
            'enabled': True,
        },
        'xwktpg3dgcxhyru7': {
            'url': 'mailto://two.f.b.kelly:kmqkhblkxavels@gmail.com?name=samuek',
            'enabled': False,
        }
    }
}


# io helpers

def _read_config():
    _path = paths.NOTIFICATION_CONFIG_PATH
    if not os.path.exists(_path):
        return DEFAULT_CONFIG
    with open(_path, 'r') as file:
        return toml.load(file)


def _write_config(config):
    with open(paths.NOTIFICATION_CONFIG_PATH, 'w') as file:
        toml.dump(config, file)

@contextmanager
def _open_config():
    config = _read_config()
    yield config
    _write_config(config)


# helpers

def _random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def _make_templates(config):
    return {
        'title': Template(config['general']['title']),
        'body': Template(config['general']['body']),
    }


# exports

def get_possible_services():
    return APPRISE.details()


def get_services():
    config = _read_config()
    return [
        {'id': id_, **service}
        for id_, service in config['services'].items()
    ]


def get_general():
    config = _read_config()
    return config['general']


def register_all():
    config = _read_config()
    APPRISE.clear()
    APPRISE.add([
        service['url']
        for service in config['services'].values()
        if service['enabled']
    ])
    

def add_service(service_type):
    service_id = _random_string(16)
    with _open_config() as config:
        config['services'][service_id] = {
            'url': '',
            'enabled': True,
        }
        return config['services'][service_id]


def update_service(service_id, service):
    with _open_config() as config:
        config['services'][service_id] = service


def remove_service(service_id):
    with _open_config() as config:
        del config['services'][service_id]
    register_all()


def send(torrent):
    config = _read_config()
    templates = _make_templates(config)
    variables = {
        'name': torrent.name,
        'id': torrent.id,
        'time': torrent.updated,
        'status': STATUS_LONG.get(
            torrent.status,                             # custom
            f'has status {torrent.status.name.lower()}' # default
        ),
    }
    APPRISE.notify(
        title=templates['title'].safe_substitute(variables),
        body=templates['body'].safe_substitute(variables),
    )
