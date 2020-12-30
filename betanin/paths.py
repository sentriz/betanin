# standard library
import os
import site
from contextlib import suppress

# 3rd party
import xdg.BaseDirectory


def _first_existing(paths):
    with suppress(StopIteration):
        return next((path for path in paths if os.path.exists(path)))


# dir
DATA_DIR = xdg.BaseDirectory.save_data_path("betanin")
CONFIG_DIR = xdg.BaseDirectory.save_config_path("betanin")
BEETS_DIR = xdg.BaseDirectory.save_config_path("beets")
CLIENT_DIST_DIR = _first_existing(
    (
        os.path.join(os.getcwd(), "betanin_client", "dist"),
        os.path.join(site.getusersitepackages(), "betanin_client", "dist"),
        os.path.join(site.getsitepackages()[0], "betanin_client", "dist"),
    )
)
MIGRATIONS_DIR = _first_existing(
    (
        os.path.join(os.getcwd(), "betanin_migrations"),
        os.path.join(site.getusersitepackages(), "betanin_migrations"),
        os.path.join(site.getsitepackages()[0], "betanin_migrations"),
    )
)

# path
BEETS_CONFIG_PATH = _first_existing(
    (
        os.path.join(BEETS_DIR, "config.yml"),
        os.path.join(BEETS_DIR, "config.yaml"),
    )
)
DB_PATH = os.path.join(DATA_DIR, "betanin.db")
SECRET_KEY_PATH = os.path.join(DATA_DIR, "secret_key")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.toml")
