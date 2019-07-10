# 3rd party
from flask_restplus import fields

# betanin
from betanin.status import Status
from betanin.rest.namespaces import META_NS
from betanin.rest.namespaces import BEETS_NS
from betanin.rest.namespaces import CLIENTS_NS
from betanin.rest.namespaces import TORRENTS_NS
from betanin.rest.namespaces import NOTIFICATIONS_NS
from betanin.rest.namespaces import AUTHENTICATION_NS


_torrent_id_field = fields.String(
    description="the id of the torrent",
    example="78d1780216dfe571b499c61e20365",
)


class _EnumField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enum_obj = kwargs.pop("enum", None)
        self.enum = enum_obj._member_names_

    @staticmethod
    def format(enum):
        return enum.name


LINE = TORRENTS_NS.model(
    "Line",
    {
        "index": fields.String(
            description="the index of the line", example="4"
        ),
        "data": fields.String(
            description="the line itself",
            example="No Xmas For John Quays -> No Xmas for John Quays",
        ),
    },
)
LINE_WITH_TORRENT_ID = TORRENTS_NS.model(
    "LineWithTorrentID", {"torrent_id": _torrent_id_field, **LINE}
)
TORRENT = TORRENTS_NS.model(
    "Torrent",
    {
        "id": _torrent_id_field,
        "path": fields.String(
            description="the path of the torrent",
            example="downloads/music/The Fall - Live at the Witch Trials (1979) [FLAC]",
        ),
        "status": _EnumField(
            description="the current status of the torrent",
            enum=Status,
            example="DOWNLOADING",
        ),
        "name": fields.String(
            description="the name of the torrent",
            example="Live at the Witch Trials",
        ),
        "has_lines": fields.Boolean(
            description="whether there are lines for the torrent or not",
            example=True,
        ),
        "tooltip": fields.String(
            description="the explained status of the torrent",
            example="torrent existed before betanin saw it",
        ),
        "updated": fields.DateTime,
        "created": fields.DateTime,
    },
)
BEETS_CONFIG = BEETS_NS.model(
    "BeetsConfig",
    {
        "time_read": fields.DateTime(
            description="the time the config was read from disk"
        ),
        "config": fields.String(
            description="the beets config (a yaml string)",
            example="""import:\nwrite: yes\nmove: yes""",
        ),
    },
)
NOTIFICATION_SERVICE = NOTIFICATIONS_NS.model(
    "NotificationService",
    {
        "id": fields.String(
            description="the unique id of the notification service",
            example="MOWP3TECHN1N8AUV",
        ),
        "type": fields.String(
            description="the type of notification service", example="E-Mail"
        ),
        "enabled": fields.Boolean(
            description="whether or not the service is enabled", example=False
        ),
        "protocol": fields.String(
            description="the apprise protocol", example="mailtos"
        ),
        "not_protocol": fields.String(
            description='the rest of the "url" of the service',
            example="person@mail.com?password=password",
        ),
    },
)
NOTIFICATION_TEST_RESULT = NOTIFICATIONS_NS.model(
    "NotificationTestResult",
    {
        "result": fields.Boolean(
            description="whether or not the test passed", example=True
        )
    },
)
NOTIFICATION_SETTINGS = NOTIFICATIONS_NS.model(
    "NotificationSettings",
    {
        "title": fields.String(
            description="the title of the notification",
            example="[betanin] torrent `$name` $status",
        ),
        "body": fields.String(
            description="the body of the notification",
            example="console: https://betanin.you.net/$console_path",
        ),
    },
)
API_KEY = CLIENTS_NS.model(
    "ClientAPIKey",
    {
        "api_key": fields.String(
            description="the client api key",
            example="d136f2db997f64d78534fadb0e2f1f2b",
        )
    },
)
AUTH_TOKEN = AUTHENTICATION_NS.model(
    "AuthToken",
    {
        "token": fields.String(
            description="the json web token for authentication",
            example="eyJAecNiOJKV1aHLCJ...",
        )
    },
)
SYSTEM_INFO = META_NS.model(
    "SystemInfo",
    {
        "platform": fields.String(
            description="the system platform name",
            example="Linux-4.9.0-8-amd64-x86_64",
        ),
        "python_version": fields.String(
            description="the system's python version", example="3.6.6"
        ),
        "betanin_version": fields.String(
            description="the running betanin version", example="0.0.3"
        ),
    },
)
SUB_DIR = META_NS.model(
    "SubDir",
    {
        "path": fields.String(
            description="the path of the dir",
            example="/downloads/september/music",
        )
    },
)
