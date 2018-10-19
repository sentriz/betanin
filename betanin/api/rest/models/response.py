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
    'remote_id': fields.Integer(
        description='the id of the remote the torrent came from',
        example='3',
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
    'has_lines': fields.Boolean(
        description='whether there are lines for the torrent or not',
        example=True,
    ),
    'tooltip': fields.String(
        description='the explained status of the torrent',
        example='torrent existed before betanin saw it',
    ),
})


fetch = torrents_ns.model('Fetch', {
    'torrents': fields.List(
        fields.Nested(torrent),
        description='the list of torrents',
    ),
    'status': fields.Raw(
        description='the global status table',
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
