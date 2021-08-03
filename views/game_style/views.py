from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.game_style import GameStyle, game_style_schema, game_styles_schema
from werkzeug.exceptions import BadRequest

from views.game_style import game_style_bp


@game_style_bp.route('/game_styles', methods=['GET', 'POST'])
@login_required
@jwt_required()
def game_styles():
    if request.method == 'GET':
        game_styles = GameStyle.query.all()
        return jsonify(game_styles_schema.dump(game_styles))

    if request.method == 'POST':
        body = request.get_json()

        try:
            name = body['name']
        except KeyError:
            raise BadRequest

        game_style = GameStyle.create(name=name)
        return jsonify(game_style_schema.dump(game_style)), status.HTTP_201_CREATED


@game_style_bp.route('/game_styles/<game_style_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
def game_style(game_style_id):
    if request.method == 'GET':
        user = GameStyle.get(game_style_id)
        return jsonify(game_style_schema.dump(user))

    if request.method == 'DELETE':
        GameStyle.delete(game_style_id)
        return jsonify({'msg': 'Game Style deleted successfully'})

    if request.method == 'PUT':
        body = request.get_json()
        GameStyle.update(game_style_id, **body)
        return jsonify({'msg': 'Game Style updated successfully'})
