import peewee
db = peewee.SqliteDatabase('database.db')


class LaunchSite(peewee.Model):

    id = peewee.CharField(primary_key=True)
    name = peewee.CharField()
    name_long = peewee.CharField()

    def get_info(self):

        info = "Launch Site Id: " + str(self.id) + "\n"
        info += "Launch Site Name: " + self.name + "\n"
        info += "Launch Site Long Name: " + self.name_long + "\n"

        return info

    class Meta:
        database = db
