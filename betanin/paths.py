# python
import os

# 3rd party
import xdg.BaseDirectory

# dir
DATA_DIR   = xdg.BaseDirectory.save_data_path('betanin')
CONFIG_DIR = xdg.BaseDirectory.save_config_path('betanin')
BEETS_DIR = os.path.expanduser('~/.config/beets/')

# path
BEETS_CONFIG_PATH = os.path.join(BEETS_DIR, 'config.yml')
DB_PATH = os.path.join(DATA_DIR, 'betanin.db')
