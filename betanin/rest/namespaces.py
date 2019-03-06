# betanin
from betanin.extensions import rest


rest.namespaces.clear()
torrents_ns = rest.namespace('torrents', description='operations related to torrents')
beets_ns = rest.namespace('beets', description='operations related to beets')
notifications_ns = rest.namespace('notifications', description='operations related to notifications')
authentication_ns = rest.namespace('authentication', description='operations related to authentication')
clients_ns = rest.namespace('clients', description='operations related to the torrent clients')
meta_ns = rest.namespace('meta', description='operations related to betanin and the current system')
