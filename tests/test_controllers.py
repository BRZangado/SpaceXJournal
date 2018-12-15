import requests
import json
import peewee

from unittest import TestCase
from controllers.DataController import DataController
from models.Launch import Launch
from models.LaunchSite import LaunchSite
from models.Rocket import Rocket

MODELS = [Launch, LaunchSite, Rocket]
test_db = peewee.SqliteDatabase(':memory:')


class DataControllerTestCase(TestCase):

    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
        self.db = DataController()
        self.api_url = "https://api.spacexdata.com/v3/launches/"

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_next_launch(self):
        self.db.get_next_launch()
        self.assertNotEqual(
            Launch.select().where(Launch.next == 1).count(),
            0
        )

    def test_next_launch_response(self):

        launch = self.db.get_next_launch()
        api_response = requests.get(self.api_url+"next")
        api_response = json.loads(api_response.text)
        self.assertEqual(
            launch.mission,
            api_response['mission_name']
        )
        self.assertNotEqual(
            Launch.select().count(),
            0
        )

    def test_latest_launch(self):
        self.db.get_latest_launch()
        self.assertNotEqual(
            Launch.select().where(Launch.latest == 1).count(),
            0
        )

    def test_upcoming_launches(self):

        self.db.get_upcoming_launches()
        self.assertNotEqual(
            Launch.select().where(Launch.upcoming == 1).count(),
            0
        )

    def test_past_launches(self):

        self.db.get_past_launches()
        self.assertNotEqual(
            Launch.select().where(Launch.past == 1).count(),
            0
        )
