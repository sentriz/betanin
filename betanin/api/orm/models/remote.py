from betanin.extensions import db

from sqlalchemy_json import NestedMutableJson


class Remote(db.Model):
    __tablename__ = 'remotes'
    id       = db.Column(db.Integer,       # unique remote id
                         primary_key=True)
    type     = db.Column(db.String)        # type of remote, eg.
                                           # transmission, deluge
    config   = db.Column(NestedMutableJson)
