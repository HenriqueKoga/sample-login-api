from core import db, ma
from marshmallow import fields
from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel

db.metadata.clear()


class Brand(db.Model, BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class BrandSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()


brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)
