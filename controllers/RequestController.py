import requests
import json


class RequestController:

    def __init__(self):
        self.api_url = "https://api.spacexdata.com/v3/launches/"
    
    def request_past_launches(self):
        response = requests.get(self.api_url+"upcoming")
        return json.loads(response.text)
    
    def request_upcoming_launches(self):
        response = requests.get(self.api_url+"past")
        return json.loads(response.text)
    
    def request_next_launch(self):
        response = requests.get(self.api_url+"next")
        return json.loads(response.text)
    
    def request_latest_launch(self):
        response = requests.get(self.api_url+"latest")
        return json.loads(response.text)

