# betanin
from betanin.api.rest.namespaces import beets_ns
from betanin.api.rest.namespaces import torrents_ns
from betanin.api.rest.namespaces import notifications_ns


# for importing a torrent
torrent = torrents_ns.parser()
torrent.add_argument(
    'name', type=str, location='form', required=True,
    help='`the name of the folder the torrent is downloaded to`',
)
torrent.add_argument(
    'path', type=str, location='form', required=True,
    help='`the download folder of torrent client (relative to betanin) '
    'for this import`',
)


# for getting a list of all torrents (paginated)
torrents = torrents_ns.parser()
torrents.add_argument(
    'page', type=int, location='args',
    help='`the page number to request`',
)
torrents.add_argument(
    'per_page', type=int, location='args',
    help='`the number of results per page`'
)


# for sending stdin to a process
line = torrents_ns.parser()
line.add_argument(
    'text', type=str, location='json', required=True,
    help='`the text data to send to process`',
)


# for configuring beets
beets_config = beets_ns.parser()
beets_config.add_argument(
    'config', type=str, location='json', required=True,
    help='`the yaml to configure beets with`',
)


# for adding a notification_service
notification_service_type = notifications_ns.parser()
notification_service_type.add_argument(
    'type', type=str, location='json', required=True,
    help='`the type of the new notification service`',
)


# for updating notification services
notification_service_list = notifications_ns.parser()
notification_service_list.add_argument(
    'services', type=list, location='json', required=True,
    help='`the list of NotificationService models`',
)

# for updating notification general settings
notification_general = notifications_ns.parser()
notification_general.add_argument(
    'title', type=str, location='json',
    help='`the new title of notifications`',
)
notification_general.add_argument(
    'body', type=str, location='json',
    help='`the new body of notifications`',
)
