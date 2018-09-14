from betanin.extensions import db

from sqlalchemy_json import NestedMutableJson


class Remote(db.Model):
    __tablename__ = 'remotes'
    id     = db.Column(db.String,
                       primary_key=True)
    fields = db.Column(NestedMutableJson)
