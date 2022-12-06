import pytest
from website.models.dbmodels import Cart,CartEntries
from website import db



# def test_cart_entry():
#     shoplist = Cart(item_name = 'Coke', quantity = 12, unit = 'Cans')
#     db.session.add(shoplist)
#     db.session.commit()


def test_cart_items():
    query= 'SELECT COUNT(*) FROM cart'
    cartcount = db.engine.execute(query)
    assert cartcount == 10
