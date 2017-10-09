from flask import flask, render template

app = Flask(__name__)

@app.route('/sign_up', methods=('GET', 'POST'))
def sign_in():
    form=register
    if form.validate_on_submit():
        return redirect('/portal)
    return render_template('sign_up.html', form=form)

if __name__ =='__main__'
    app.run(debug='True')


