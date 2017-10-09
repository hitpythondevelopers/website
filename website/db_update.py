from datetime import date

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from website import db 

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from website.database import metadata, db_session

class User(db.Model, UserMixin):
   
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(80), unique=True)
    twitter_handle = db.Column(db.String(80),unique=True)
    password_hash = db.Column(db.String(80))
   
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password_hash)