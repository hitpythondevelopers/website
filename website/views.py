from flask import render_template,  flash, redirect, url_for, session,request, logging
from passlib.hash import sha256_crypt

from website import app
from forms import RegisterForm

#from website.database import db_session


@app.route('/')
def index():
    #posts = Blogpost.query.all()
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
        
        return redirect(url_for('index'))


    return render_template('register.html', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'GET' and form.validate():

        username = form.username.data
        password = sha256_crypt.decrypt(str(form.password.data))

        return redirect(url_for('index'))
    return render_template('login.html', form = form)


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

