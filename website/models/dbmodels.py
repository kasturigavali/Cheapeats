from website import db
from sqlalchemy.sql import func
from datetime import date

class CartEntries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    store_name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True) , default= date.today())
    sl_item = db.Column(db.Integer, db.ForeignKey('cart.id'))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50))
    quantity = db.Column(db.Integer, default=1)
    unit = db.Column(db.String(10))
    cartentries = db.relationship('CartEntries')


