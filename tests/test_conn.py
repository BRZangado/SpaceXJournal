import requests

from unittest import TestCase


class ApiRequestsTestCase(TestCase):

    def setUp(self):
        self.api_url = "https://api.spacexdata.com/v3/launches/"

    def tearDown(self):
        del self.api_url

    def test_status_code(self):
        response = requests.get(self.api_url)
        self.assertTrue(response.status_code == requests.codes.ok)

    def test_status_next_endpoint(self):
        response_next = requests.get(self.api_url+"next")
        self.assertTrue(response_next.status_code == requests.codes.ok)

    def test_status_upcoming_endpoint(self):
        response_upcoming = requests.get(self.api_url+"upcoming")
        self.assertTrue(response_upcoming.status_code == requests.codes.ok)

    def test_status_past_endpoint(self):
        response_past = requests.get(self.api_url+"past")
        self.assertTrue(response_past.status_code == requests.codes.ok)

    def test_status_latest_endpoint(self):
        response_latest = requests.get(self.api_url+"latest")
        self.assertTrue(response_latest.status_code == requests.codes.ok)
