from flask_login import UserMixin

from .app import db
from sqlalchemy import Column, Integer, String


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
