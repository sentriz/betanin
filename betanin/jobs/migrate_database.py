# 3rd party
from flask_migrate import upgrade

# betanin
from betanin import paths


def _start():
    upgrade(directory=paths.MIGRATIONS_DIR)


def start(flask_app):
    with flask_app.app_context():
        _start()
