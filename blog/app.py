from os import getenv, path

from flask import Flask
from json import load

from flask_sqlalchemy import SQLAlchemy

from blog.auth.views import auth
from blog.article.views import article
from blog.user.views import user

CONF_PATH = getenv('CONF_PATH', path.join('../conf.json'))

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    # app.config.from_file(CONF_PATH, load)
    app.config['SECRET_KEY'] = 'cu@jp62kq@_=fkzg5xkl@v_zr-(g4o8pz@k6d4zd-tc@mj+b)u'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    from .models import User
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
