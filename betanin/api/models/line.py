from betanin.extensions import db


class Line(db.Model):
    __tablename__ = 'lines'
    id            = db.Column(db.Integer,
                              primary_key=True)
    index         = db.Column(db.Integer)
    data          = db.Column(db.String)
    torrent_id    = db.Column(db.String, 
                              db.ForeignKey('torrents.id'))
