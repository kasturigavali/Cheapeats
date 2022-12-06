import pytest
from website import create_app
from flask.testing import FlaskClient



@pytest.fixture(scope='module')
def app():
    app = create_app()
    return app

