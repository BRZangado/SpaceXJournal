import requests
import json


class RequestController:

    api_url = "https://api.spacexdata.com/v3/launches/"

    @classmethod
    def request_past_launches(cls):
        response = requests.get(cls.api_url+"upcoming")
        return json.loads(response.text)

    @classmethod
    def request_upcoming_launches(cls):
        response = requests.get(cls.api_url+"past")
        return json.loads(response.text)

    @classmethod
    def request_next_launch(cls):
        response = requests.get(cls.api_url+"next")
        return json.loads(response.text)

    @classmethod
    def request_latest_launch(cls):
        response = requests.get(cls.api_url+"latest")
        return json.loads(response.text)
