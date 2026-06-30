import requests
import pytest
from urls import URL
from data import order_data

class TestCreateOrder:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = order_data.copy()
        payload['color'] = color
        response = requests.post(URL + '/api/v1/orders', json=payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()