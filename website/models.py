from datetime import date

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from website import db 

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from yourapplication.database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None, username = None, password = None):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
    Column('username', VarChar(120), unique=True)
    Column('password', VarChar(120), unique=True)
)
mapper(User, users)