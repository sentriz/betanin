from betanin.api.orm.models.line import Line
from betanin.api.status import Status
from betanin.extensions import db


class Torrent(db.Model):
    __tablename__ = 'torrents'
    id             = db.Column(db.String,
                               primary_key=True)
    name           = db.Column(db.String)
    path           = db.Column(db.String)
    status         = db.Column(db.Enum(Status))
    lines          = db.relationship('Line')

    def __str__(self):
        return f'Torrent({self.status})'

    @property
    def has_lines(self):
        return len(self.lines) != 0

    def delete_lines(self):
        Line.query.filter_by(torrent_id=self.id).delete()

    def add_line(self, index, data):
        self.lines.append(Line(
            index=index,
            data=data,
        ))
