from betanin.extensions import db
from betanin.api.status import RemoteStatus
from betanin.api.status import BetaStatus


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id            = db.Column(db.String,
                              primary_key=True)
    name          = db.Column(db.String)
    path          = db.Column(db.String)
    remote_status = db.Column(db.Enum(RemoteStatus,
                              default=RemoteStatus.UNKNOWN))
    beta_status   = db.Column(db.Enum(BetaStatus),
                              default=BetaStatus.UNKNOWN)
    progress      = db.Column(db.Float)

    @classmethod
    def from_dict(cls, torrent_dict):
        return cls(**torrent_dict)

    @classmethod
    def update_or_create(cls, torrent_dict):
        torrent_id = torrent_dict['id']
        existing = cls.query.filter_by(id=torrent_id)
        assert existing.count() in (0, 1)
        if existing.count() == 1:
            existing.update(torrent_dict)
            return existing.first()
        else:
            return cls.from_dict(torrent_dict)



