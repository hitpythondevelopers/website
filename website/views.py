from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

from yourapplication.database import db_session


@app.route('/')
def index():
    return render_template('index.html')


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


<<<<<<< HEAD
    return render_template('register.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
=======
    return render_template('register.html', form=form)
>>>>>>> 30726528512e24ed955a889d752146562efb471b
