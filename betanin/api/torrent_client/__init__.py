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

def _get_torrents_with_extras(map_dict_items_row):
    remote_id, client = map_dict_items_row
    return map(lambda torrent_dict: {'remote_id': remote_id,
                                     **torrent_dict},
               client.get_torrents())

# /end of internals


CLIENTS = {} # a map of remote ids to `Client`s


def get_remote_names():
	return list(_remote_wrappers.keys())


def get_torrents():
    return chain(*map(
        _get_torrents_with_extras,
        CLIENTS.items(), # ((remote_id, dict)...)
    ))


def get_default_config(remote_name):
    return _remote_wrappers[remote_name].DEFAULT_CONFIG


def make_all_sessions():
    'called on startup'
    CLIENTS = []
    for remote in Remote.query.all():
       update_session(remote) 


def update_session(remote):
    'called by `PUT /settings/remotes/<remote_id>/config`'
    wrapper = _remote_wrappers[remote.type]
    # a this point the config might be completely wrong. 
    # the user mightn't have pressed the 'test'
    # button yet, and we don't want to test the connection
    # unless we're asked. so we must make exceptions.
    try:
        client = wrapper.Client(remote)
    except Exception as exc:
        print(f'exception while creating client for {remote}: {exc}')
        return
    CLIENTS[remote.id] = client


def test_connection(remote_id):
    if not remote_id in CLIENTS:
        return False, 'could not create session'
    session = CLIENTS[remote_id]
    return session.test_connection()
