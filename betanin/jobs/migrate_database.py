# 3rd party
from flask_migrate import upgrade

# betanin
from betanin import paths


def start(flask_app):
    with flask_app.app_context():
        upgrade(directory=paths.MIGRATIONS_DIR)
