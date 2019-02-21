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
        example='downloads/music/The Fall - Live at the Witch Trials (1979) [FLAC]',
    ),
    'status': _EnumField(
        description='the current status of the torrent',
        enum=Status,
        example='DOWNLOADING',
    ),
    'name': fields.String(
        description='the name of the torrent',
        example='Live at the Witch Trials',
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

beets_config = torrents_ns.model('BeetsConfig', {
    'time_read': fields.DateTime(
        description='the time the config was read from disk',
    ),
    'config': fields.String(
        description='the beets config (a yaml string)',
        example='''import:\nwrite: yes\nmove: yes''',
    ),
})

notification_service = torrents_ns.model('NotificationService', {
    'id': fields.String(
        description='the unique id of the notification service',
        example='MOWP3TECHN1N8AUV',
    ),
    'type': fields.String(
        description='the type of notification service',
        example='E-Mail',
    ),
    'enabled': fields.Boolean(
        description='whether or not the service is enabled',
        example=False,
    ),
    'protocol': fields.String(
        description='the apprise protocol',
        example='mailtos',
    ),
    'not_protocol': fields.String(
        description='the rest of the "url" of the service',
        example='person@mail.com?password=password',
    ),
})

notification_test_result = torrents_ns.model('NotificationTestResult', {
    'result': fields.Boolean(
        description='whether or not the test passed',
        example=True,
    ),
})

notification_settings = torrents_ns.model('NotificationSettings', {
    'title': fields.String(
        description='the title of the notification',
        example='[betanin] torrent `$name` $status',
    ),
    'body': fields.String(
        description='the body of the notification',
        example='console: https://betanin.you.net/$console_path',
    )
})

api_key = torrents_ns.model('ClientAPIKey', {
    'api_key': fields.String(
        description='the client api key',
        example='d136f2db997f64d78534fadb0e2f1f2b',
    ),
})

auth_token = torrents_ns.model('AuthToken', {
    'token': fields.String(
        description='the json web token for authentication',
        example='eyJAecNiOJKV1aHLCJ...',
    ),
})
