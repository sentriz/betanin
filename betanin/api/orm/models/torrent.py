# betanin
from betanin.api.status import Status
from betanin.extensions import db
from betanin.api.orm.models.line import Line


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id      = db.Column(db.String,
                        primary_key=True)
    name    = db.Column(db.String)
    path    = db.Column(db.String)
    status  = db.Column(db.Enum(Status))
    created = db.Column(db.DateTime, default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    lines   = db.relationship('Line')

    def __str__(self):
        return f'Torrent({self.status})'

    @property
    def has_lines(self):
        return len(self.lines) != 0

    @property
    def last_line_index(self):
        return max(line.index for line in self.lines) \
            if self.lines else -1

    def delete_lines(self):
        Line.query.filter_by(torrent_id=self.id).delete()

    def add_line(self, index, data):
        self.lines.append(Line(
            index=index,
            data=data,
        ))
