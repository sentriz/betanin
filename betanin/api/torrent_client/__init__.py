import importlib
from betanin import bet_config


_client = bet_config.CLIENT
_client_package_name = f'betanin.api.torrent_client.{_client}'
_client_globals = importlib.import_module(_client_package_name).__dict__

globals().update(_client_globals)
