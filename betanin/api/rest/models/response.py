from betanin.api.rest.namespaces import torrents_ns
from betanin.api.status import BetaStatus
from betanin.api.status import RemoteStatus

from flask_restplus import fields


class _EnumField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enum_obj = kwargs.pop('enum', None)
        self.enum = enum_obj._member_names_

    @staticmethod
    def format(enum):
        return enum.name


line = torrents_ns.model('Line', {
    'index': fields.String(
        description='the index of the line',
        example='4',
    ),
    'data': fields.String(
        description='the line itself',
        example='dfksjhfshdfdfksdhfj',
    ),
})


torrent = torrents_ns.model('Torrent', {
    'id': fields.String(
        description='the id of the torrent',
        example='kfjhkdjfghkdfjghdkijfhg',
    ),
    'path': fields.String(
        description='the path of the torrent',
        example='downloads/music/Sam - Sammy (2014) [FLAC]',
    ),
    'progress': fields.Fixed(
        description='the current download progress of the torrent',
        example=34.76,
        decimals=2,
    ),
    'remote_status': _EnumField(
        description='the current status of the torrent',
        enum=RemoteStatus,
        example='COMPLETED'
    ),
    'beta_status': _EnumField(
        description='the current status of the torrent',
        enum=BetaStatus,
        example='COMPLETED',
    ),
    'name': fields.String(
        description='the name of the torrent',
        example='Sammy',
    ),
    'tooltip': fields.String(
        description='the explained status of the torrent',
        example='torrent existed before betanin saw it',
    ),
})


remote = torrents_ns.model('Remote', {
    'id': fields.Integer(
        description='the unique id of the remote',
        example='2',
    ),
    'type': fields.String(
        description='the type of the remote',
        example='transmission',
    ),
    'config': fields.Raw(
        description='the config of the remote',
    )
})
