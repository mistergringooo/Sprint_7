from registration_courier import register_new_courier_and_return_login_password
import pytest
import requests
from urls import URL

@pytest.fixture
def courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass

    login_payload = {"login": login_pass[0], "password": login_pass[1]}
    response = requests.post(URL + '/api/v1/courier/login', json=login_payload)
    if response.status_code == 200:
        courier_id = response.json()['id']
        requests.delete(URL + f'/api/v1/courier/{courier_id}')

@pytest.fixture
def delete_courier():
    created_couriers = []

    def _delete(login, password):
        created_couriers.append((login, password))

    yield _delete

    for login, password in created_couriers:
        login_payload = {"login": login, "password": password}
        response = requests.post(URL + '/api/v1/courier/login', json=login_payload)
        if response.status_code == 200:
            courier_id = response.json()['id']
            requests.delete(URL + f'/api/v1/courier/{courier_id}')