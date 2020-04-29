# betanin
from betanin.status import Status
from betanin.extensions import DB


class Line(DB.Model):
    __tablename__ = "lines"
    id = DB.Column(DB.Integer, primary_key=True)
    index = DB.Column(DB.Integer)
    data = DB.Column(DB.String)
    torrent_id = DB.Column(DB.Integer, DB.ForeignKey("torrents.id"))


class Torrent(DB.Model):
    __tablename__ = "torrents"
    __table_args__ = {"sqlite_autoincrement": True}
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    path = DB.Column(DB.String)
    status = DB.Column(DB.Enum(Status))
    created = DB.Column(DB.DateTime, default=DB.func.now())
    updated = DB.Column(
        DB.DateTime, default=DB.func.now(), onupdate=DB.func.now()
    )
    lines = DB.relationship("Line", cascade="all, delete")

    def __str__(self):
        return f"Torrent({self.status})"

    @property
    def has_lines(self):
        return len(self.lines) != 0

    def add_line(self, line):
        line.index = len(self.lines) + 1
        self.lines.append(line)
