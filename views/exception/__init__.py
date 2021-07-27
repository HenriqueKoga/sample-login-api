from flask import Blueprint

error_bp = Blueprint('error', __name__)

if True:
    from . import views
