import uuid

from flask import jsonify, request
from flask_api import status
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.user import User, user_schema, users_schema
from services.crypto.crypto import create_bcrypt_hash
from werkzeug.exceptions import BadRequest

from views.user import user_bp


@user_bp.route('/users', methods=['GET', 'POST'])
@login_required
@jwt_required()
def users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    if request.method == 'POST':
        body = request.get_json()

        try:
            name = body['name']
            username = body['username']
            email = body['email']
            password = body['password']
        except KeyError:
            raise BadRequest

        user_id = str(uuid.uuid4())
        password_crypt = create_bcrypt_hash(password)

        user = User.create(**{
            'id': user_id,
            'name': name,
            'email': email,
            'username': username,
            'password': password_crypt,
            'photo': None
        })
        return jsonify(user_schema.dump(user)), status.HTTP_201_CREATED


@user_bp.route('/users/<user_id>', methods=['GET', 'DELETE'])
@login_required
def user(user_id):
    if request.method == 'GET':
        user = User.get(user_id)
        return jsonify(user_schema.dump(user))

    if request.method == 'DELETE':
        User.delete(user_id)
        return jsonify({'msg': 'User deleted successfully'})
