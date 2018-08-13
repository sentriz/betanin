from betanin.extensions import db
from betanin.api.status import RemoteStatus
from betanin.api.status import BetaStatus


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id            = db.Column(db.String,
                              primary_key=True)
    name          = db.Column(db.String)
    path          = db.Column(db.String)
    remote_status = db.Column(db.Enum(RemoteStatus))
    beta_status   = db.Column(db.Enum(BetaStatus))
