import xdg.BaseDirectory
import sys
import os


_data_dir   = xdg.BaseDirectory.save_data_path('betamin')
_config_dir = xdg.BaseDirectory.save_config_path('betamin')
PICKLE_PATH = os.path.join(_data_dir, 'state.pickle')
sys.path.append(_config_dir)

try:
    config = __import__('config')
except ModuleNotFoundError:
    print('config file not found', file=sys.stderr)
    sys.exit(1)
