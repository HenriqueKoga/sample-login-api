from core import db, ma
from flask_login import UserMixin

from models.base_model import BaseModel

db.metadata.clear()


class User(db.Model, UserMixin, BaseModel):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    photo = db.Column(db.String(255))


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'photo')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
