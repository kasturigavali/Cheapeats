from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE']

@app.route('/')
def home():
    return render_template('index.html')
    # return '<h2>Hello, World! Welcome to <sub>Cheap</sub>Eats</h2>'

@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('psw')
        confirm_password = request.form.get('repeat-psw')
    return render_template("index.html")


@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('psw')
    return render_template("/login.html")

@app.route('/shoppingcart')
def shoppingcart():
    return render_template("/shoppingcart.html")



if __name__ == '__main__':
    app.run(debug=True,port=8000)
