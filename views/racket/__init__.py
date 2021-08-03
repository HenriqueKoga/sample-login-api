from flask import Blueprint

racket_bp = Blueprint('racket', __name__)

if True:
    from . import views
