from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.rubber import Rubber, rubber_schema, rubbers_schema
from werkzeug.exceptions import BadRequest

from views.rubber import rubber_bp


@rubber_bp.route('/rubbers', methods=['GET', 'POST'])
@login_required
@jwt_required()
def rubbers():
    if request.method == 'GET':
        rubbers = Rubber.query.all()
        return jsonify(rubbers_schema.dump(rubbers))

    if request.method == 'POST':
        body = request.get_json()

        try:
            name = body['name']
            color = body['color']
            brand_id = body['brand_id']
        except KeyError:
            raise BadRequest

        rubber = Rubber.create(
            name=name,
            color=color,
            brand_id=brand_id
        )
        return jsonify(rubber_schema.dump(rubber)), status.HTTP_201_CREATED


@rubber_bp.route('/rubbers/<rubber_id>', methods=['GET', 'DELETE'])
@login_required
def rubber(rubber_id):
    if request.method == 'GET':
        user = Rubber.get(rubber_id)
        return jsonify(rubber_schema.dump(user))

    if request.method == 'DELETE':
        Rubber.delete(rubber_id)
        return jsonify({'msg': 'Rubber deleted successfully'})
