import sys
from app import paths


# config dir has 'config.py'
sys.path.append(paths.CONFIG_DIR)

try:
    from config import *
except ModuleNotFoundError:
    print('config file not found', file=sys.stderr)
    sys.exit(1)
