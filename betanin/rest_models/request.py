# betanin
from betanin.rest.namespaces import META_NS
from betanin.rest.namespaces import BEETS_NS
from betanin.rest.namespaces import TORRENTS_NS
from betanin.rest.namespaces import NOTIFICATIONS_NS
from betanin.rest.namespaces import AUTHENTICATION_NS


# for importing a torrent
TORRENT = TORRENTS_NS.parser()
TORRENT.add_argument(
    "name",
    type=str,
    location="form",
    help="`the name of the folder the torrent is downloaded to`",
)
TORRENT.add_argument(
    "path",
    type=str,
    location="form",
    help="`the download folder of torrent client (relative to betanin) "
    "for this import`",
)
TORRENT.add_argument(
    "both",
    type=str,
    location="form",
    help="`the full path to torrent (same as both args)`",
)


# for getting a list of all torrents (paginated)
TORRENTS = TORRENTS_NS.parser()
TORRENTS.add_argument(
    "page",
    type=int,
    location="args",
    help="`the page number to request (when paginating)`",
)
TORRENTS.add_argument(
    "per_page",
    type=int,
    location="args",
    help="`the number of results per page (when paginating)`",
)


# for sending stdin to a process
LINE = TORRENTS_NS.parser()
LINE.add_argument(
    "text",
    type=str,
    location="json",
    required=True,
    help="`the text data to send to process`",
)


# for configuring beets
BEETS_CONFIG = BEETS_NS.parser()
BEETS_CONFIG.add_argument(
    "config",
    type=str,
    location="json",
    required=True,
    help="`the yaml to configure beets with`",
)


# for adding a notification_service
NOTIFICATION_SERVICE_TYPE = NOTIFICATIONS_NS.parser()
NOTIFICATION_SERVICE_TYPE.add_argument(
    "type",
    type=str,
    location="json",
    required=True,
    help="`the type of the new notification service`",
)

# for updating notification services
NOTIFICATION_SERVICE_LIST = NOTIFICATIONS_NS.parser()
NOTIFICATION_SERVICE_LIST.add_argument(
    "services",
    type=list,
    location="json",
    required=True,
    help="`the list of NotificationService models`",
)


# for updating notification strings settings
NOTIFICATION_STRINGS = NOTIFICATIONS_NS.parser()
NOTIFICATION_STRINGS.add_argument(
    "title", type=str, location="json", help="`the new title of notifications`"
)
NOTIFICATION_STRINGS.add_argument(
    "body", type=str, location="json", help="`the new body of notifications`"
)


# for logging the user and getting a jwt
CREDENTIALS = AUTHENTICATION_NS.parser()
CREDENTIALS.add_argument(
    "username",
    type=str,
    location="json",
    required=True,
    help="`the username to authenticate with`",
)
CREDENTIALS.add_argument(
    "password",
    type=str,
    location="json",
    required=True,
    help="`the password to authenticate with`",
)


# for getting sub dirs with manual import
SUB_DIRS = META_NS.parser()
SUB_DIRS.add_argument(
    "dir",
    type=str,
    location="args",
    required=True,
    help="`the directory you want the sub directories of`",
)
