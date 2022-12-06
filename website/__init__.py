from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path


DB_NAME = "cheapeats.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    return app

def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
        



