from flask import render_template

from website import app

@app.route('/')
def index():
	title = "FnF Up"
    return render_template('index.html', title=title)