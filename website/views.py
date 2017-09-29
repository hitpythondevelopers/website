from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from website import app

@app.route('/')
def index():
    return render_template('index.html')



#implementing the registration form with validation
class RegisterForm(Form):
	name = StringField('Name',[validators.Length(min=1, max= 50)])
	username = StringField('Username',[validators.Length(min=4,max=25)])
	email = StringField('Email',[validators.Length(min=6, max =50)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message='Password does not match')

	])
	confirm = PasswordField('Confirm Password')


#routing the register request
@app.route('/register', methods =['GET','POST'])
def register():
    form = RegisterForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
        return render_template('register.html')


    return render_template('register.html')