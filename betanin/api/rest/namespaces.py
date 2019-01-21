# betanin
from betanin.extensions import rest


rest.namespaces.clear()
torrents_ns = rest.namespace('torrents', description='operations related to torrents')
beets_ns = rest.namespace('beets', description='operations related to beets')
notifications_ns = rest.namespace('notifications', description='operations related to notifications')
