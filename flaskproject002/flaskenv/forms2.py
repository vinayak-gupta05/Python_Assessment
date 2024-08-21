from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process form data here
        return redirect(url_for('welcome'))
    return render_template('login.html', form=form)

@app.route('/welcome')
def welcome():
    return 'Hello, welcome to the application!'
