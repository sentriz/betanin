# betanin
from betanin.extensions import DB


class Line(DB.Model):
    __tablename__ = "lines"
    id = DB.Column(DB.Integer, primary_key=True)
    index = DB.Column(DB.Integer)
    data = DB.Column(DB.String)
    torrent_id = DB.Column(DB.Integer, DB.ForeignKey("torrents.id"))
