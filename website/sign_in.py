from datetime import date

from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField
from wtforms.validators import DataRequired

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from website import db 




app = Flask(__name__)

class Register(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    phone number = StringField('phone', validators=[DataRequired()])
    twitter handle = StringField('twitter', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    recaptcha = RecaptchaField()

class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])



@app.route('/sign_up', methods=('GET', 'POST'))
def sign_in():
    form=Register
    if form.validate_on_submit():
        return redirect('/portal')
    return render_template('sign_up.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    form=Login
    if form.validate_on_submit():
        return redirect('/portal')
    return render_template('login.html', form=form)



if __name__ =='__main__'
    app.run(debug='True')


