from flask import Blueprint

game_style_bp = Blueprint('game_style', __name__)

if True:
    from . import views
