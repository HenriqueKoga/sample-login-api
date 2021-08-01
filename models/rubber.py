from core import db, ma
from marshmallow import fields
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.brand import Brand, brand_schema

db.metadata.clear()


class Rubber(db.Model, BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    color = Column(String(50), nullable=False)
    brand_id = Column(Integer, ForeignKey(Brand.id))

    brand = relationship(Brand)


class RubberSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    color = fields.String()
    brand = fields.Nested(brand_schema)


rubber_schema = RubberSchema()
rubbers_schema = RubberSchema(many=True)
