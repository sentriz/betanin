# python
import os

# 3rd party
import xdg.BaseDirectory


def _first_existing(*paths):
    return next((
        path \
        for path in paths \
        if os.path.exists(path)
    ))

# dir
DATA_DIR = xdg.BaseDirectory.save_data_path('betanin')
CONFIG_DIR = xdg.BaseDirectory.save_config_path('betanin')
BEETS_DIR = os.path.expanduser('~/.config/beets/')

# path
BEETS_CONFIG_PATH = _first_existing(
    os.path.join(BEETS_DIR, 'config.yml'),
    os.path.join(BEETS_DIR, 'config.yaml'),
)
DB_PATH = os.path.join(DATA_DIR, 'betanin.db')
NOTIFICATION_CONFIG_PATH = os.path.join(CONFIG_DIR, 'notifications.toml')
