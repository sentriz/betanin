from betanin.extensions import db

from sqlalchemy_json import NestedMutableJson


class Remote(db.Model):
    __tablename__ = 'remotes'
    id        = db.Column(db.Integer,       # unique remote id
                          primary_key=True)
    type      = db.Column(db.String)        # type of remote, eg.
                                            # transmission, deluge
    config    = db.Column(NestedMutableJson)
    is_in_use = db.Column(db.Boolean,
                          default=False)
    torrents  = db.relationship('Torrent', backref='remote')

    @classmethod
    def delete_unused(cls):
        cls.query.filter_by(is_in_use=False).delete()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    def __repr__(self):
        return f'Remote(id={self.id}, type={self.type})'
