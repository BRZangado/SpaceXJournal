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
    
    def get_next_launch(self):

        try:
            launch = Launch.get(Launch.next == 1)
            return launch
        except Launch.DoesNotExist:
            self.populate_next_launch()
    
    def get_latest_launch(self):

        try:
            launch = Launch.get(Launch.latest == 1)
            return launch
        except Launch.DoesNotExist:
            return self.populate_latest_launch()
    
    def get_upcoming_launches(self):

        launches = Launch.select().where(Launch.upcoming == 1)
        if len(launches) == 0:
            print("buscando lançamentos")
            return self.populate_upcoming_launches()
        print("mostrando lançamentos")
        return launches
    
    def get_past_launches(self):
        
        launches = Launch.select().where(Launch.past == 1)
        if len(launches) == 0:
            print("buscando lançamentos")
            return self.populate_past_launches()
        print("mostrando lançamentos")
        return launches
    
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
        return launch
    
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
        return launch
    
    def populate_past_launches(self):

        saved_launches = []
        data = self.request_controller.request_past_launches()

        for record in data:
            rocket = self.save_rocket(record.pop('rocket'))
            launchsite = self.save_launch_site(record.pop('launch_site'))
            launch = self.save_launch(
                record,
                launchsite,
                rocket,
                ['past']
            )
            saved_launches.append(launch)
        
        return saved_launches
    
    def populate_upcoming_launches(self):

        saved_launches = []
        data = self.request_controller.request_upcoming_launches()

        for record in data:
            rocket = self.save_rocket(record.pop('rocket'))
            launchsite = self.save_launch_site(record.pop('launch_site'))
            launch = self.save_launch(
                record,
                launchsite,
                rocket,
                ['upcoming']
            )
            saved_launches.append(launch)
        
        return saved_launches
    
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

