from os.path import join,dirname, realpath

from flask import Flask 
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from flask_basicauth import BasicAuth


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#db = SQLAlchemy(app)
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.session_protection = "strong"
#login_manager.login_view = "login"
#basic_auth = BasicAuth(app)


from website import views 
