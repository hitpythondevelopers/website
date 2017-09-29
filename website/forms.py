import datetime

from flask_wtf import FlaskForm 
from wtforms.fields import SelectField, FloatField, TextAreaField, StringField, PasswordField, FileField, BooleanField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, url, Length, Email, Regexp, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


#implementing the registration form with validation
class RegisterForm(FlaskForm):
	name = StringField('Name',[validators.Length(min=1, max= 50)])
	username = StringField('Username',[validators.Length(min=4,max=25)])
	email = StringField('Email',[validators.Length(min=6, max =50)])
	password = PasswordField('Password',[
		validators.DataRequired(),
		validators.EqualTo('confirm',message='Password does not match')

	])
	confirm = PasswordField('Confirm Password')


