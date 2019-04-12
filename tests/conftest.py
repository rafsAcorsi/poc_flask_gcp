# encoding: utf-8
"""Conf test"""

import pytest

from main import create_app


@pytest.fixture
def client():
    app = create_app().app
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        yield client
