import requests
import pytest
from urls import URL

class TestOrdersList:
    def test_orders_list(self):
        response = requests.get(URL + '/api/v1/orders')
        
        assert response.status_code == 200
        assert 'orders' in response.json()