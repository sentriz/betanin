# 3rd party
from flask_restplus import fields

# betanin
from betanin.api.status import Status
from betanin.api.rest.namespaces import torrents_ns


class _EnumField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enum_obj = kwargs.pop('enum', None)
        self.enum = enum_obj._member_names_

    @staticmethod
    def format(enum):
        return enum.name


_torrent_id_field = fields.String(
    description='the id of the torrent',
    example='78d1780216dfe571b499c61e20365',
)

line = torrents_ns.model('Line', {
    'index': fields.String(
        description='the index of the line',
        example='4',
    ),
    'data': fields.String(
        description='the line itself',
        example='No Xmas For John Quays -> No Xmas for John Quays',
    ),
})

line_with_torrent_id = torrents_ns.model('LineWithTorrentID', {
    'torrent_id': _torrent_id_field,
    **line,
})

torrent = torrents_ns.model('Torrent', {
    'id': _torrent_id_field,
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
    'updated': fields.DateTime,
    'created': fields.DateTime,
})
