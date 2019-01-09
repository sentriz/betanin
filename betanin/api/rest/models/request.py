# 3rd party
from flask_restplus import fields

# betanin
from betanin.api.rest.namespaces import torrents_ns

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


line = torrents_ns.parser()
line.add_argument(
    'text', type=str, location='json', required=True,
    help='`the text data to send to process`',
)
