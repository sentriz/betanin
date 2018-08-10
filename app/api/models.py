from app.api.torrent_client import RemoteStatus
from app.api.torrent_client import BetaStatus


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id            = db.Column(db.String,
                              primary_key=True)
    name          = db.Column(db.String)
    path          = db.Column(db.String)
    remote_status = db.Column(db.Enum(RemoteStatus))
    beta_status   = db.Column(db.Enum(BetaStatus))
