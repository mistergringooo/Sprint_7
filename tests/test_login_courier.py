import requests
import pytest
from urls import URL
from registration_courier import register_new_courier_and_return_login_password
from data import no_login
from data import no_password

class TestCourierLogin:
    def test_courier_login(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        response = requests.post(URL + '/api/v1/courier/login', json=payload)
        
        assert response.status_code == 200
        assert response.json()['id'] is not None

    def test_login_with_wrong_credentials(self, courier):
        payload = {
            "login": courier[0],
            "password": "wrong_password"
        }
        response = requests.post(URL + '/api/v1/courier/login', json=payload)
        
        assert response.status_code == 404

    @pytest.mark.parametrize('payload', [no_login, no_password])
    def test_login_missing_field(self, payload):
        response = requests.post(URL + '/api/v1/courier/login', json=payload)
        
        assert response.status_code in [400, 504]

    def test_login_nonexistent_courier(self):
        payload = {
            "login": "nonexistent_login",
            "password": "nonexistent_password"
        }
        response = requests.post(URL + '/api/v1/courier/login', json=payload)
        
        assert response.status_code == 404