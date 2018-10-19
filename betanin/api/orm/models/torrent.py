from betanin.api.orm.models.line import Line
from betanin.api.status import BetaStatus
from betanin.api.status import RemoteStatus
from betanin.extensions import db


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
    lines          = db.relationship('Line')

    def __str__(self):
        return f'Torrent({self.remote_status}, {self.beta_status})'

    @property
    def has_lines(self):
        return len(self.lines) != 0

    @classmethod
    def get_or_create(cls, torrent_id):
        existing = cls.query.filter_by(id=torrent_id)
        assert existing.count() in (0, 1)
        if existing.count() == 1:
            return existing.first()
        else:
            return cls(id=torrent_id)

    def set_status(self, status, reason=None):
        if isinstance(status, RemoteStatus):
            self.remote_status = status
        elif isinstance(status, BetaStatus):
            self.beta_status = status
        else:
            raise ValueError('unknown status type')
        self.tooltip = reason

    def has_status(self, status):
        return self.beta_status == status or \
            self.remote_status == status

    def delete_lines(self):
        Line.query.filter_by(torrent_id=self.id).delete()

    def add_line(self, index, data):
        self.lines.append(Line(
            index=index,
            data=data,
        ))
