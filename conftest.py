from registration_courier import register_new_courier_and_return_login_password
import pytest

@pytest.fixture
def courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass