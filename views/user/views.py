from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_login import login_required
from models.user import User, user_schema, users_schema

from views.user import user_bp


@user_bp.route("/users")
@login_required
@jwt_required()
def users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))


@user_bp.route("/users/<user_id>")
@login_required
def user(user_id):
    user = User.get(user_id)
    return jsonify(user_schema.dump(user))
