from betanin.api.rest.namespaces import torrents_ns

from flask_restplus import fields


line = torrents_ns.model('Line', {
    'text': fields.String(required=True)
})


torrent = torrents_ns.model('Torrent', {
    'id': fields.String(required=True),
    'path': fields.String(required=True),
})
