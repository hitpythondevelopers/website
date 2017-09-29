from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

@app.route('/')
def home():
    return render_template('index.html')


#routing the register request
@app.route('/register', methods =['GET','POST'])
def index():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

    return render_template('index.html')