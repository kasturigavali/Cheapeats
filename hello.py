from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE'] = "sqlite:///cheapeats.db"

@app.route('/')
def home():
    return render_template('index.html')
    # return '<h2>Hello, World! Welcome to <sub>Cheap</sub>Eats</h2>'


@app.route('/shoppingcart')
def shoppingcart():
    return render_template("/shoppingcart.html")



if __name__ == '__main__':
    app.run(debug=True,port=8000)
