"""Tests for hero api"""


def test_get_heroes(client):
    response = client.get('/api/hero/search')
    assert response.status_code == 200
