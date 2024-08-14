import datetime
import random
from random import uniform
from faker import Faker
from py_client.shared_functions import ApiTest, get_auth_credentials, create_headers


fake = Faker()


class AuthCredentials:
    username = "root"
    password = "123456"


def create_random_product(number_of_products):
    token_auth = get_auth_credentials(username=AuthCredentials.username, password=AuthCredentials.password)
    ApiTest.prefix = '/products/product/list?limit=100'
    products_response = ApiTest.get(headers=create_headers(token=token_auth))
    if products_response.json:
        return

    for number_of_product in range(number_of_products):
        price = round(float(uniform(10.01, 99.99)), 2)
        token_auth = get_auth_credentials(username=AuthCredentials.username, password=AuthCredentials.password)
        ApiTest.prefix = '/products/product/create'
        ApiTest.json_add = {
            "price": price, "name": fake.name(), "content": fake.text(max_nb_chars=35), "title": fake.job()
        }
        post_response = ApiTest.post(headers=create_headers(token=token_auth))
        print('post_response', post_response.json)
        print('post_response', post_response.status)


def create_random_product_comment(number_of_products):
    token_auth = get_auth_credentials(username=AuthCredentials.username, password=AuthCredentials.password)
    ApiTest.prefix = '/products/product/list?limit=100'
    products_response = ApiTest.get(headers=create_headers(token=token_auth))
    products_list = products_response.json['results']
    for number_of_product in range(number_of_products):
        random_product = random.choice(products_list)
        selected_product = random_product['uu_id']
        ApiTest.prefix = "/products/comment/create"
        ApiTest.json_add = {
                "comment": fake.text(max_nb_chars=55),
                "product": selected_product,
                "created_at": datetime.datetime.now().__str__()
            }
        products_response = ApiTest.post(headers=create_headers(token=token_auth))


def create_random_product_rating(number_of_products):
    token_auth = get_auth_credentials(username=AuthCredentials.username, password=AuthCredentials.password)
    ApiTest.prefix = '/api/user/list'
    user_response = ApiTest.get(headers=create_headers(token=token_auth))
    if not user_response.json:
        raise Exception('First create a user object')

    users_list = user_response.json['results']
    user_id = users_list[0].get('id')

    ApiTest.prefix = '/products/product/list?limit=100'
    products_response = ApiTest.get(headers=create_headers(token=token_auth))
    products_list = products_response.json['results']

    for number_of_product in range(number_of_products):
        random_product = random.choice(products_list)
        selected_product = random_product['uu_id']
        ApiTest.prefix = "/products/rating/create"
        ApiTest.json_add = {
                "user": user_id,
                "product": selected_product,
                "rating": random.randint(1, 5)
            }
        products_response = ApiTest.post(headers=create_headers(token=token_auth))



create_random_product(100)
create_random_product_comment(100)
create_random_product_rating(100)
