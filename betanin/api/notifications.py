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
    'services': {}
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

def register_all():
    config = _read_config()
    APPRISE.clear()
    APPRISE.add([
        f'{service["protocol"]}://{service["not_protocol"]}'
        for service in config['services'].values()
        if all(
            service[key]
            for key in ('enabled', 'protocol', 'not_protocol')
        )
    ])
    

def get_possible_services():
    return APPRISE.details()


def get_services():
    with _open_config() as config:
        # remove incomplete services
        config['services'] = {
            service_id: service \
            for service_id, service in config['services'].items() \
            if service['not_protocol']
        }
        return config['services']


def get_general():
    config = _read_config()
    return config['general']


def add_service(service_type):
    service_id = _random_string(16)
    with _open_config() as config:
        config['services'][service_id] = {
            'type': service_type,
            'enabled': True,
            'protocol': '',
            'not_protocol': '',
        }
        return {
            'id': service_id,
            **config['services'][service_id]
        }


def update_services(services):
    with _open_config() as config:
        config['services'] = services


def update_general(general):
    with _open_config() as config:
        config['general'] = general


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
