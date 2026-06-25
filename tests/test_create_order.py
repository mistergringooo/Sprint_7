import requests
import pytest
from urls import URL

class TestCreateOrder:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(URL + '/api/v1/orders', json=payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()