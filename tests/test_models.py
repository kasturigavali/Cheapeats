import pytest
from website.models.dbmodels import Cart,CartEntries
from website import db


def test_cart_items(app):
    testcount = None
    with app.app_context():
        query= 'SELECT COUNT(*) AS count FROM cart'
        cartcount = db.engine.execute(query)
        for row in cartcount:
            print(row)
            testcount = row.count
        assert testcount == 10

@pytest.mark.parametrize('url', [('/shoppingcart'), ('/static/style.css'), ('/static/img1.jpg'), ('/static/cheapeats.png')])
def test_shoppingcart(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 200


@pytest.mark.parametrize('url', [('/dashboard'), ('/static/style.css'), ('/static/img1.jpg'), ('/static/cheapeats.png')])
def test_dashboard(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 200


@pytest.mark.parametrize('url', [('/'), ('/static/style.css'), ('/static/img1.jpg'), ('/static/cheapeats.png')])
def test_index(app, url):
    with app.test_client() as test_client:
        test = test_client.get(url)
    assert test.status_code == 200


