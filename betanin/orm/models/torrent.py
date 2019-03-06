# betanin
from betanin.status import Status
from betanin.extensions import db


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id = db.Column(db.String,
        primary_key=True)
    name = db.Column(db.String)
    path = db.Column(db.String)
    status = db.Column(db.Enum(Status))
    created = db.Column(db.DateTime,
        default=db.func.now())
    updated = db.Column(db.DateTime,
        default=db.func.now(),
        onupdate=db.func.now())
    lines = db.relationship('Line',
        cascade="all, delete")

    def __str__(self):
        return f'Torrent({self.status})'

    @property
    def has_lines(self):
        return len(self.lines) != 0

    def add_line(self, line):
        line.index = len(self.lines) + 1
        self.lines.append(line)
