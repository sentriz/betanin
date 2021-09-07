# standard library
import os
from contextlib import contextmanager

# 3rd party
import toml

# betanin
from betanin import paths


DEFAULT_CONFIG = {
    "frontend": {"username": "", "password": ""},
    "notifications": {
        "services": {},
        "strings": {
            "body": "@ $time. view/use the console at http://127.0.0.1:9393/$console_path",
            "title": "[betanin] torrent `$name` $status",
        },
    },
    "clients": {"api_key": ""},
    "server": {"num_parallel_jobs": 1},
}


def gen_api_key(length=16):
    return os.urandom(length).hex()


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


def find_creds_correct(conf, username, password):
    return (
        username == conf["frontend"]["username"]
        and password == conf["frontend"]["password"]
    )


def find_api_key(conf):
    return conf["clients"]["api_key"]


def find_api_key_correct(conf, api_key):
    return conf["clients"]["api_key"] == api_key


def find_num_parallel_jobs(conf):
    return conf.get("server", {}).get("num_parallel_jobs", 1)
