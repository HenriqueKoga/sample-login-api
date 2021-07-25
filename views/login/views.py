from core import login_manager
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from models.user import User
from services.crypto.crypto import verify_password
from services.google_auth.google_auth import GoogleAuth

from views.login import login_bp


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_bp.route("/")
def index():
    if current_user.is_authenticated:
        return render_template(
            'home.html',
            name=current_user.name,
            email=current_user.email,
            photo=current_user.photo
        )
    else:
        return render_template('login.html')


@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        google_auth = GoogleAuth()
        request_uri = google_auth.get_request_uri()
        return redirect(request_uri)

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.get(username=username)
        if user:
            is_valid = verify_password(password, user.password)
            if is_valid:
                login_user(user)
                return redirect(url_for("login.index"))
        return 'invalid username/password'


@login_bp.route("/login/callback")
def callback():
    google_auth = GoogleAuth()
    user = google_auth.get_user()
    login_user(user)
    return redirect(url_for("login.index"))


@login_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.index"))