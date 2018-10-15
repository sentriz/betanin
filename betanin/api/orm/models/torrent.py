from betanin.api.orm.models.line import Line
from betanin.api.status import BetaStatus
from betanin.api.status import RemoteStatus
from betanin.extensions import db


def _enum_value_from_string(enum, string):
    return getattr(enum, string.upper())


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id             = db.Column(db.String,
                               primary_key=True)
    name           = db.Column(db.String)
    path           = db.Column(db.String)
    remote_status  = db.Column(db.Enum(RemoteStatus),
                               default=RemoteStatus.UNKNOWN)
    beta_status    = db.Column(db.Enum(BetaStatus),
                               default=BetaStatus.UNKNOWN)
    progress       = db.Column(db.Float)
    should_process = db.Column(db.Boolean,
                               default=False)
    tooltip        = db.Column(db.String)
    remote_id      = db.Column(db.Integer, db.ForeignKey('remotes.id'))
    lines          = db.relationship("Line")

    @classmethod
    def get_or_create(cls, torrent_id):
        existing = cls.query.filter_by(id=torrent_id)
        assert existing.count() in (0, 1)
        if existing.count() == 1:
            return existing.first()
        else:
            return cls(id=torrent_id)

    def set_beta_status(self, status, reason=None):
        self.beta_status = _enum_value_from_string(BetaStatus, status)
        self.tooltip = reason

    def set_remote_status(self, status):
        self.remote_status = _enum_value_from_string(RemoteStatus, status)

    def delete_lines(self):
        Line.query.filter_by(torrent_id=self.id).delete()

    def add_line(self, index, data):
        self.lines.append(Line(
            index=index,
            data=data,
        ))
