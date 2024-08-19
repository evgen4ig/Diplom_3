import random
import allure
import string
import requests

import data
from data import Url


@allure.step('Генерируем рандомную строку')
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерируем рандомный email')
def generate_random_email():
    return f'{generate_random_string()}@gmail.com'


@allure.step('Регистрируем нового пользователя и возвращаем его данные')
def register_new_user_and_return_user_data():

    user_data = {}

    email = generate_random_email()
    password = generate_random_string()
    name = generate_random_string()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }

    response = requests.post(Url.CREATE_USER_HANDLE, data=payload)

    if response.status_code == 200:
        user_data = {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': response.json()
        }

    return user_data


@allure.step('Удаляем пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.DELETE_USER_HANDLE, headers=headers)


@allure.step('Создаем заказ')
def create_order(user):
    payload = {
        'ingredients': [data.TestData.INGREDIENTS]
    }
    headers = {'Authorization': user['json']['accessToken']}
    response = requests.post(Url.ORDERS_HANDLE, data=payload, headers=headers)
    return response