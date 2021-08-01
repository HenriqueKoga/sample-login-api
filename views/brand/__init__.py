from flask import Blueprint

brand_bp = Blueprint('brand', __name__)

if True:
    from . import views
