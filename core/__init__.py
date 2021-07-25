import os

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = os.getcwd()


app = Flask(__name__, template_folder=f'{basedir}/templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/dev.db"
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)


db = SQLAlchemy(app)
ma = Marshmallow(app)


if True:
    from views.login import login_bp
    from views.user import user_bp
    from views.register import register_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(register_bp)
