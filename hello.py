from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h2>Hello, World! Welcome to <sub>Cheap</sub>Eats</h2>'