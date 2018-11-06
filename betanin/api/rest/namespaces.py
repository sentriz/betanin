# betanin
from betanin.extensions import rest

rest.namespaces.clear()
torrents_ns = rest.namespace('torrents', description='operations related to torrents')
settings_ns = rest.namespace('settings', description='operations related to settings')
