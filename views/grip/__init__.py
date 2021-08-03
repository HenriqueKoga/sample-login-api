from flask import Blueprint

grip_bp = Blueprint('grip', __name__)

if True:
    from . import views
