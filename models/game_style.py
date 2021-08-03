from core import db, ma
from marshmallow import fields
from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel

db.metadata.clear()


class GameStyle(db.Model, BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class GameStyleSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()


game_style_schema = GameStyleSchema()
game_styles_schema = GameStyleSchema(many=True)
