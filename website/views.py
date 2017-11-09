from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

<<<<<<< HEAD
from website.database import db_session
=======
#from website.database import db_session
>>>>>>> master


@app.route('/')
def index():
<<<<<<< HEAD
=======
    #posts = Blogpost.query.all()
>>>>>>> master
    return render_template('index.html')


#routing the register request
<<<<<<< HEAD
@app.route('/Register', methods =['GET','POST'])
def Register():
    form = Register_Form(request.form)
=======
@app.route('/register', methods =['GET','POST'])
def register():
    form = RegisterForm(request.form)
>>>>>>> master
    
    if request.method == 'POST' and form.validate():
        
        name = form.name.data
<<<<<<< HEAD
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
=======
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
>>>>>>> master
        
        return redirect(url_for('index'))


<<<<<<< HEAD
    return render_template('Register.html', form=form)

@app.route('/Login', methods = ['GET','POST'])
=======
    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET','POST'])
>>>>>>> master
def login():
    form = LoginForm(request.form)

    if request.method == 'GET' and form.validate():

        username = form.username.data
        password = sha256_crypt.decrypt(str(form.password.data))

        return redirect(url_for('index'))
    return render_template('login.html', form = form)

<<<<<<< HEAD
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
=======

@app.route('/post')
def post1():
    return render_template('post.html')
    



@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    date_posted = post.date_posted.strftime('%B %d , %Y')
    return render_template('post.html', post=post)
@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods = ['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    
    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

>>>>>>> master
