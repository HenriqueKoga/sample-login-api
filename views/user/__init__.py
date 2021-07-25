from flask import Blueprint

user_bp = Blueprint('user', __name__)

if True:
    from . import views
