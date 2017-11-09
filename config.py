# this file contains all your application's configuration settings

import os 
from os.path import join,dirname, realpath

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#SQLALCHEMY CONFIGURATIONS
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'website.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#FLASK-BASICAUTH CONFIGURATIONS
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'admin'

#Uploads 
UPLOAD_FOLDER_LOGO = join(dirname(realpath(__file__)), 'static/images/')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])