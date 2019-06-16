from flask_login import UserMixin
from app import db

class Users(UserMixin, db.Model):
    # todo model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    roles = db.Column(db.Integer)