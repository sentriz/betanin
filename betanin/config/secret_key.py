# standard library
import os

# betanin
from betanin import paths


def gen(length=32):
    return os.urandom(length).hex()


def write(key):
    with open(paths.SECRET_KEY_PATH, "w") as file:
        file.write(key)


def read():
    with open(paths.SECRET_KEY_PATH, "r") as file:
        return file.read()
