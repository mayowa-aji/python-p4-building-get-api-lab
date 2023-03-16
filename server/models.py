from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.dialects.sqlite import DATETIME

db = SQLAlchemy()
dt = DATETIME()
class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ("-baked_goods.bakery",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.String, server_default=db.func.now())
    updated_at = db.Column(db.String, onupdate=db.func.now())

    baked_goods= db.relationship('BakedGood', backref='bakery')

    def __repr__(self):
        return f'<Bakery {self.name}>'


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ("-bakeries.baked_goods",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    created_at = db.Column(db.String, server_default = db.func.now() )
    updated_at = db.Column(db.String, onupdate=db.func.now())
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

def __repr__(self):
        return f'<Baked Good {self.name}, ${self.price}>'


