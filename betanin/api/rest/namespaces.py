from betanin.api import api_rest


api_rest.namespaces.clear()
torrents_ns = api_rest.namespace('torrents', description='operations related to torrents')
settings_ns = api_rest.namespace('settings', description='operations related to settings')
