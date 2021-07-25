import uuid

from flask import render_template, request
from models.user import User
from services.crypto.crypto import create_bcrypt_hash

from views.register import register_bp


@register_bp.route("/register", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user_id = str(uuid.uuid4())
        password_crypt = create_bcrypt_hash(password)

        User.create(**{
            'id': user_id,
            'name': name,
            'email': email,
            'username': username,
            'password': password_crypt,
            'photo': None
        })
        return render_template('register.html')
