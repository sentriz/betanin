import importlib
from betanin.config import client


_client = client.CLIENT
_client_package_name = f'betanin.api.torrent_client.{_client}'
_client_globals = importlib.import_module(_client_package_name).__dict__

globals().update(_client_globals)
