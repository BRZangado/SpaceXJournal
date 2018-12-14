import peewee

from controllers.RequestController import RequestController
from models.Launch import Launch
from models.LaunchSite import LaunchSite
from models.Rocket import Rocket


class DataController:

    def __init__(self):
        self.request_controller = RequestController()

    def init_database(self):

        try:
            Launch.create_table()
            LaunchSite.create_table()
            Rocket.create_table()
            print("TABELAS CRIADAS")

        except peewee.OperationalError as err:
            print(err)
    
    def populate_next_launch(self):

        data = self.request_controller.request_next_launch()
        rocket = self.save_rocket(data.pop('rocket'))
        launchsite = self.save_launch_site(data.pop('launch_site'))
        launch = self.save_launch(
            data,
            launchsite,
            rocket,
            ['next', 'upcoming']
        )
        print(launch.get_info())
    
    def populate_latest_launch(self):

        data = self.request_controller.request_latest_launch()
        rocket = self.save_rocket(data.pop('rocket'))
        launchsite = self.save_launch_site(data.pop('launch_site'))
        launch = self.save_launch(
            data,
            launchsite,
            rocket,
            ['latest', 'past']
        )
        print(launch.get_info())
    
    def populate_past_launches(self):

        data = self.request_controller.request_past_launches()
        for record in data:
            rocket = self.save_rocket(record.pop('rocket'))
            launchsite = self.save_launch_site(record.pop('launch_site'))
            launch = self.save_launch(
                record,
                launchsite,
                rocket,
                ['latest', 'past']
            )
            print(launch.get_info())
    
    def populate_upcoming_launches(self):

        data = self.request_controller.request_upcoming_launches()
        for record in data:
            rocket = self.save_rocket(record.pop('rocket'))
            launchsite = self.save_launch_site(record.pop('launch_site'))
            launch = self.save_launch(
                record,
                launchsite,
                rocket,
                ['latest', 'past']
            )
            print(launch.get_info())
    
    def save_rocket(self, data):

        rocket = Rocket.create(
            id=data['rocket_id'],
            name=data['rocket_name'],
            r_type=data['rocket_type']
        )
        return rocket

    def save_launch_site(self, data):
        
        launch_site = LaunchSite.create(
            id = data['site_id'],
            name = data['site_name'],
            name_long = data['site_name_long']
        )
        return launch_site

    def save_launch(self, data, launch_site, rocket, status):
        
        launch = Launch.create(
            mission = data['mission_name'],
            flight_number = data['flight_number'],
            date=data['launch_date_local'],
            rocket=rocket,
            launch_site=launch_site,
        )

        if('next' in status):
            launch.next = 1
        if('upcoming' in status):
            launch.upcoming = 1
        if('past' in status):
            launch.past = 1
        if('latest' in status):
            launch.latest = 1
        
        launch.save()
        return launch

