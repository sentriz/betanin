# 3rd party
from flask_restplus import fields

# betanin
from betanin.api.rest.namespaces import torrents_ns


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
