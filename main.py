from controllers.DataController import DataController

if __name__ == '__main__':

    db = DataController()
    db.init_database()
    db.populate_next_launch()