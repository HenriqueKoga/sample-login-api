from core import db, ma
from marshmallow import fields
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.brand import Brand, brand_schema
from models.rubber import Rubber, rubber_schema

db.metadata.clear()


class Racket(db.Model, BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    brand_id = Column(Integer, ForeignKey(Brand.id))
    forehand_rubber_id = Column(Integer, ForeignKey(Rubber.id))
    backhand_rubber_id = Column(Integer, ForeignKey(Rubber.id))

    brand = relationship(Brand)
    forehand_rubber = relationship(Rubber, foreign_keys=[forehand_rubber_id])
    backhand_rubber = relationship(Rubber, foreign_keys=[backhand_rubber_id])


class RacketSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    brand = fields.Nested(brand_schema)
    forehand_rubber = fields.Nested(rubber_schema)
    backhand_rubber = fields.Nested(rubber_schema)


racket_schema = RacketSchema()
rackets_schema = RacketSchema(many=True)
