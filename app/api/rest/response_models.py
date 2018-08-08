from app.api import torrent_client
from app.api.rest.namespaces import torrents_ns
from flask_restplus import fields


class _EnumField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enum_obj = kwargs.pop('enum', None)
        self.enum = enum_obj._member_names_

    def format(self, enum):
        return enum.name


torrent = torrents_ns.model('Torrent', {
    'id': fields.String(
        description='the id of the torrent',
        example='kfjhkdjfghkdfjghdkijfhg',
    ),
    'path': fields.String(
        description='the path of the torrent',
        example='downloads/music/Sam - Sammy (2014) [FLAC]',
    ),
    'progress': fields.Float(
        description='the current download progress of the torrent',
        example=34.76,
    ),
    'status': _EnumField(
        description='the current status of the torrent',
        enum=torrent_client.Status,
        example=torrent_client.Status._member_names_[0],
    ),
    'name': fields.String(
        description='the name of the torrent',
        example='Sammy',
    ),
})
