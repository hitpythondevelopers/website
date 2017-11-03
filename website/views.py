from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

from website.database import db_session


@app.route('/')
def index():
    return render_template('index.html')


#routing the register request
@app.route('/Register', methods =['GET','POST'])
def Register():
    form = Register_Form(request.form)
    
    if request.method == 'POST' and form.validate():
        
        name = form.name.data
        session['name'] = name
        date_of_birth = form.date_of_birth.data
        session['date_of_birth'] = date_of_birth
        email = form.email.data
        session['email'] = email
        username = form.username.data
        session['username'] = username
        phone_number = form.phonenumber.data
        session['phone_number'] = phine_number
        twitter_handle = form.twitter.data
        session['twitter_handle'] = twitter_handle
        facebook = form.facebook.data
        session['facebook'] = facebook
        password = sha256_crypt.encrypt(str(form.password.data))
        session['password'] = password
        
        return redirect(url_for('index'))


    return render_template('Register.html', form=form)

@app.route('/Login', methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'GET' and form.validate():

        username = form.username.data
        password = sha256_crypt.decrypt(str(form.password.data))

        return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/unregister')
def unregister():
    # Make sure they've already registered the member
    if User not in session:
        return "You are not registered!"
    User = session[User]
    # Make sure the memebr was already in the list
    if User not in Users:
        return "That member isn't on our list"
    Users.remove(user)
    del session[User] # Make sure to remove the member from the session
    return 'We have removed ' + User + ' from the list!'

    return '<h1>Title: {}  Subtitle: {} Author: {} Content: {}</h1>'.format(title, subtitle, author, content)
