from app import db

class Registrs(db.Model):
    __tablename__ = 'registrs'

    regcode = db.Column(db.String(11), index=True, unique=True, primary_key=True )
    sepa = db.Column(db.String(18))
    name = db.Column(db.String(254))
    name_before_quotes = db.Column(db.String(254))
    name_in_quotes = db.Column(db.String(254))
    name_after_quotes = db.Column(db.String(254))
    without_quotes = db.Column(db.String(254))
    regtype = db.Column(db.String(1))
    regtype_text = db.Column(db.String(60))
    type = db.Column(db.String(3))
    type_text = db.Column(db.String(60))
    registered = db.Column(db.Date)
    terminated = db.Column(db.Date)
    closed = db.Column(db.String(1))
    address = db.Column(db.String(120))
    index = db.Column(db.String)
    addressid = db.Column(db.Integer)
    region = db.Column(db.Integer)
    city = db.Column(db.Integer)
    atvk = db.Column(db.String(7))

    def __init__(self, **kwargs):
        super(Registrs, self).__init__(**kwargs)

    def __repr__(self):
        return '<regcode {}>'.format(self.regcode)