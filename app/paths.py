import xdg.BaseDirectory
import os


DATA_DIR   = xdg.BaseDirectory.save_data_path('betanin')
CONFIG_DIR = xdg.BaseDirectory.save_config_path('betanin')
DB_PATH = os.path.join(DATA_DIR, 'betanin.db')
