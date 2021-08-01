from flask import Blueprint

rubber_bp = Blueprint('rubber', __name__)

if True:
    from . import views
