from flask import Blueprint

register_bp = Blueprint('register', __name__)

if True:
    from . import views
