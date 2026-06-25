import requests
import pytest
from urls import URL
from registration_courier import register_new_courier_and_return_login_password
from data import no_login
from data import no_password
import random
import string

class TestCourierCreate:
    def test_create_courier(self):
        payload = {
            "login": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "password": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "firstName": ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        }
        response = requests.post(URL + '/api/v1/courier', json=payload)
        
        assert response.status_code == 201
        assert response.json()['ok'] == True

    def test_create_duplicate_courier(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        requests.post(URL + '/api/v1/courier', json=payload)
        response = requests.post(URL + '/api/v1/courier', json=payload)
    
        assert response.status_code == 409

    @pytest.mark.parametrize('payload', [no_login, no_password])
    def test_create_courier_missing_field(self, payload):
        response = requests.post(URL + '/api/v1/courier', json=payload)
            
        assert response.status_code == 400