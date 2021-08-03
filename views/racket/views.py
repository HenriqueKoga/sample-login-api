from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.racket import Racket, racket_schema, rackets_schema
from werkzeug.exceptions import BadRequest

from views.racket import racket_bp


@racket_bp.route('/rackets', methods=['GET', 'POST'])
@login_required
@jwt_required()
def rackets():
    if request.method == 'GET':
        rackets = Racket.query.all()
        return jsonify(rackets_schema.dump(rackets))

    if request.method == 'POST':
        body = request.get_json()
        racket = Racket.create(**body)
        return jsonify(racket_schema.dump(racket)), status.HTTP_201_CREATED


@racket_bp.route('/rackets/<racket_id>', methods=['GET', 'DELETE', 'PUT'])
@login_required
def racket(racket_id):
    if request.method == 'GET':
        user = Racket.get(racket_id)
        return jsonify(racket_schema.dump(user))

    if request.method == 'DELETE':
        Racket.delete(racket_id)
        return jsonify({'msg': 'Racket deleted successfully'})

    if request.method == 'PUT':
        body = request.get_json()
        Racket.update(racket_id, **body)
        return jsonify({'msg': 'Racket updated successfully'})
