from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/index.html')
def home():
    return render_template('index.html')
    # return '<h2>Hello, World! Welcome to <sub>Cheap</sub>Eats</h2>'

# @app.route()
# def login():
#     return renter_template('login.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
