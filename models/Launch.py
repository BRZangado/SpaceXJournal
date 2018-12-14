import peewee
from models.Rocket import Rocket
from models.LaunchSite import LaunchSite

db = peewee.SqliteDatabase('database.db')


class Launch(peewee.Model):

    id = peewee.AutoField()
    mission = peewee.CharField()
    flight_number = peewee.IntegerField()
    date = peewee.CharField()
    upcoming = peewee.SmallIntegerField(null = True)
    past = peewee.SmallIntegerField(null = True)
    next = peewee.SmallIntegerField(null = True)
    latest = peewee.SmallIntegerField(null = True)
    rocket = peewee.ForeignKeyField(
        Rocket,
        backref='Launchs'
    )
    launch_site = peewee.ForeignKeyField(
        LaunchSite,
        backref='Launchs'
    )

    def get_info(self):

        info = "Mission name: " + self.mission + "\n"
        info += "Flight Number: " + str(self.flight_number) + "\n"
        info += "Date: " + self.date + "\n"
        info += self.rocket.get_info()
        info += self.launch_site.get_info()

        return info
    
    class Meta:
        database = db