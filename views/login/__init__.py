from flask import Blueprint

login_bp = Blueprint('login', __name__)

if True:
    from . import views
