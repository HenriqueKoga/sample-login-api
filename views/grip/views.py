from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.grip import Grip, grip_schema, grips_schema
from werkzeug.exceptions import BadRequest

from views.grip import grip_bp


@grip_bp.route('/grips', methods=['GET', 'POST'])
@login_required
@jwt_required()
def grips():
    if request.method == 'GET':
        grips = Grip.query.all()
        return jsonify(grips_schema.dump(grips))

    if request.method == 'POST':
        body = request.get_json()

        try:
            name = body['name']
        except KeyError:
            raise BadRequest

        grip = Grip.create(name=name)
        return jsonify(grip_schema.dump(grip)), status.HTTP_201_CREATED


@grip_bp.route('/grips/<grip_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
def grip(grip_id):
    if request.method == 'GET':
        user = Grip.get(grip_id)
        return jsonify(grip_schema.dump(user))

    if request.method == 'DELETE':
        Grip.delete(grip_id)
        return jsonify({'msg': 'Grip deleted successfully'})

    if request.method == 'PUT':
        body = request.get_json()
        Grip.update(grip_id, **body)
        return jsonify({'msg': 'Grip updated successfully'})
