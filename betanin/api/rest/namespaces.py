# betanin
from betanin.extensions import rest

rest.namespaces.clear()
torrents_ns = rest.namespace('torrents', description='operations related to torrents')
