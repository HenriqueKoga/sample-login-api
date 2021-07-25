from flask import jsonify
from flask_login import login_required
from models.user import User, users_schema

from views.user import user_bp


@user_bp.route("/users")
@login_required
def users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))
