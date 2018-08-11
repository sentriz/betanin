from functools import reduce

from app.api.rest.namespaces import torrents_ns
from app.api.status import BetaStatus
from app.api.status import RemoteStatus

from flask_restplus import fields



class _EnumsField(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        enums = kwargs.pop('enums', None)
        self.enum = reduce(
            lambda total, e: [
                *total, 
                *[f'{e.__name__}.{f.name}' for f in e]
            ],
            enums, 
            []
        )


torrent = torrents_ns.model('Torrent', {
    'id': fields.String(
        description='the id of the torrent',
        example='kfjhkdjfghkdfjghdkijfhg',
    ),
    'path': fields.String(
        description='the path of the torrent',
        example='downloads/music/Sam - Sammy (2014) [FLAC]',
    ),
    'progress': fields.Fixed(
        description='the current download progress of the torrent',
        example=34.76,
        decimals=2,
    ),
    'status': _EnumsField(
        description='the current status of the torrent',
        enums=(RemoteStatus, BetaStatus),
        example='RemoteStatus.COMPLETED'
    ),
    'name': fields.String(
        description='the name of the torrent',
        example='Sammy',
    ),
})
