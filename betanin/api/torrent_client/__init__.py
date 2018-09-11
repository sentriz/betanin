from betanin.config import client

import os.path
import imp


def _remote_name(filename):
	# at this point we know the filename ends with '.py'
	return filename[:-3]


def _qual_remote_name(name):
	return f'remotes.{name}'


def _list_remotes():
	for remote_file in os.listdir(_this_dir):
		remote_path = os.path.join(_this_dir, remote_file)
		if not os.path.isfile(remote_path):
			continue
		if remote_file.startswith('_'):
			continue
		if not remote_file.endswith('.py'):
			continue
		remote_name = _remote_name(remote_file)
		yield remote_name, remote_path


def _load_remote(name, path):
    return imp.load_source(
		_qual_remote_name(name),
		path
	)


_this_dir = os.path.dirname(__file__)
_remotes = {
	name: _load_remote(name, path) \
		for name, path in _list_remotes()
}


def get_remote_names():
	return list(_remotes.keys())


# TODO: not this
_client = client.CLIENT
_client_globals = _remotes[_client].__dict__
globals().update(_client_globals)
