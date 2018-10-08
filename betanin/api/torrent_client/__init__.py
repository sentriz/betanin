import os.path
import imp
from itertools import chain
from collections import namedtuple
from betanin.api.orm.models.remote import Remote


def _remote_name(filename):
	# at this point we know the filename ends with '.py'
	return filename[:-3]


def _qual_remote_name(name):
	return f'remotes.{name}'


def _list_remote_wrappers():
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
_remote_wrappers = {
	name: _load_remote(name, path) \
		for name, path in _list_remote_wrappers()
}


# /end of internals


SessionInfo = namedtuple('SessionInfo', 'remote_id remote_name session torrent_getter')
SESSIONS = [] # a list of `SessionInfo`s


def get_remote_names():
	return list(_remote_wrappers.keys())


def get_torrents():
    return chain(*map(
        lambda session_info: s_info.torrent_getter(s_info.session),
        SESSIONS,
    ))


def get_default_config(remote_name):
    return _remote_wrappers[remote_name].DEFAULT_CONFIG


def make_sessions():
    for remote in Remote.query.all():
        wrapper = _remote_wrappers[remote.name]
        SESSIONS.append = SessionInfo(remote.id,
                                      remote.name,
                                      wrapper.create_session(remote.config),
                                      wrapper.get_torrents)
