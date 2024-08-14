import requests

from typing import Optional
from config_reader import grab_settings_dict


def get_auth_credentials(username: str, password: str):
    ApiTest.prefix = '/products/auth'
    ApiTest.json_add = {"username": username, "password": password, "next": "/admin"}
    post_response = ApiTest.post()
    return post_response.json.get('token')


def create_headers(token: str = None):
    default_headers = {
        "Content-Type": "application/json",

    }
    if token:
        default_headers['Authorization'] = f"Bearer {token}"
    return default_headers

class Endpoint:
    base_url: str = grab_settings_dict['api_base_url']
    prefix: str
    params: Optional[dict] = None
    json_add: Optional[dict] = None

    @classmethod
    def get_url(cls, prefix: str = None):
        if prefix:
            cls.prefix = prefix
        if not cls.prefix:
            raise Exception('Give prefix to continue')
        if cls.base_url[-1] == '/':
            cls.base_url = cls.base_url[:-1]
        if cls.prefix[0] == '/':
            cls.prefix = cls.prefix[1:]
        return cls.base_url + '/' + (cls.prefix if cls.prefix else "")


class Response:

    def __init__(
            self, status, response, text: str = None, json: dict = None
    ):
        self.response = response
        self.status: int = status
        self.text: Optional[str] = text if text else ""
        self.json: Optional[dict] = json if json else {}


class ApiTest(Endpoint):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_json_and_text(response):
        json, text = {}, ""
        try:
            json = response.json()
        except Exception as e:
            err = e
        try:
            text = response.text
        except Exception as e:
            err = e
        return json, text

    @classmethod
    def get(cls, headers: dict = None):
        response = requests.get(
            cls.get_url(),
            params=dict(cls.params) if cls.params else None,
            json=dict(cls.json_add) if cls.json_add else None,
            headers=headers or {}
        )
        json, text = cls.get_json_and_text(response=response)
        return Response(
            response=response,
            status=int(response.status_code),
            text=text,
            json=json
        )

    @classmethod
    def put(cls):
        response = requests.put(
            cls.get_url(),
            params=dict(cls.params) if cls.params else None,
            json=dict(cls.json_add) if cls.json_add else None
        )
        json, text = cls.get_json_and_text(response=response)
        return Response(
            response=response,
            status=int(response.status_code),
            text=text,
            json=json
        )

    @classmethod
    def post(cls, headers: dict = None):
        response = requests.post(
            cls.get_url(),
            params=dict(cls.params) if cls.params else None,
            json=dict(cls.json_add) if cls.json_add else None,
            headers=headers or {}
        )
        json, text = cls.get_json_and_text(response=response)
        return Response(
            response=response,
            status=int(response.status_code),
            text=text,
            json=json,
        )

