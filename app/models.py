#!/usr/bin/env python

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Users(UserMixin, db.Model):
    # todo model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    roles = db.Column(db.Integer)
    verified = db.Column(db.Integer)

    # https://dev.to/kaelscion/authentication-hashing-in-sqlalchemy-1bem
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)