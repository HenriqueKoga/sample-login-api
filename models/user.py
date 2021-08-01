from core import db, ma
from marshmallow import fields
from flask_login import UserMixin
from sqlalchemy import Column, String

from models.base_model import BaseModel

db.metadata.clear()


class User(db.Model, UserMixin, BaseModel):
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50))
    photo = Column(String(255))


class UserSchema(ma.Schema):
    id = fields.String()
    name = fields.String()
    email = fields.String()
    username = fields.String()
    photo = fields.String()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
