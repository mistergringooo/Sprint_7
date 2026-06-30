import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

no_login = {"password": generate_random_string(10), "firstName": generate_random_string(10)}
no_password = {"login": generate_random_string(10), "firstName": generate_random_string(10)}
no_firstName = {"login": generate_random_string(10), "password": generate_random_string(10)}
order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha"
}