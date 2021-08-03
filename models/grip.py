from core import db, ma
from marshmallow import fields
from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel

db.metadata.clear()


class Grip(db.Model, BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class GripSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()


grip_schema = GripSchema()
grips_schema = GripSchema(many=True)
