from os import getenv, path

from flask import Flask

from .extension import db, login_manager

from blog.auth.views import auth
from blog.article.views import article
from blog.main.views import main
from .models import User
from blog.user.views import user

base_dir = path.abspath(path.dirname(__file__))


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cu@jp62kq@_=fkzg5xkl@v_zr-(g4o8pz@k6d4zd-tc@mj+b)u'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(base_dir, 'app.db')

    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(main)
