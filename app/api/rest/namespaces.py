from app.api import api_rest


api_rest.namespaces.clear()
api_rest.namespace('torrents', description='operations related to torrents')
api_rest.namespace('settings', description='operations related to settings')
