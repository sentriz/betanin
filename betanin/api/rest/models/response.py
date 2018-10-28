from betanin.api.rest.namespaces import torrents_ns
from betanin.api.status import Status

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
    'status': _EnumField(
        description='the current status of the torrent',
        enum=Status,
        example='DOWNLOADING',
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
