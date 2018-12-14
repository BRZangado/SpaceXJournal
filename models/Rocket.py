import peewee
db = peewee.SqliteDatabase('database.db')


class Rocket(peewee.Model):

    id = peewee.CharField(primary_key=True)
    name = peewee.CharField()
    r_type = peewee.CharField()

    def get_info(self):

        info = "Rocket Id: " + str(self.id) + "\n"
        info += "Rocket Name: " + self.name + "\n"
        info += "Rocker Type: " + self.r_type + "\n"

        return info

    class Meta:
        database = db
