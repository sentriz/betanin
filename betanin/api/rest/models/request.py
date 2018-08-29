from betanin.api.rest.namespaces import torrents_ns

from flask_restplus import fields


line = torrents_ns.model('Line', {
    'text': fields.String(required=True)
})
