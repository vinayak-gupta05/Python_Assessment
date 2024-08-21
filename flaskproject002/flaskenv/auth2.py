from flask import Flask
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
    return 'Welcome to the main page!'