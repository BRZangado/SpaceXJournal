from controllers.DataController import DataController


class Console:

    db = DataController()

    @classmethod
    def start(cls):

        print("\n\n")
        print(" ----- Bem vindo ao Space X Journal -----")
        print(" Confira os dados dos lançamentos da SpaceX ")

        while True:

            print("\n")
            print("O que deseja consultar?")
            print("(1) Próximo lançamento")
            print("(2) Último lançamento")
            print("(3) Próximos lançamentos")
            print("(4) Últimos lançamentos")
            print("(5) Sair")
            print("\n")

            option = input("Selecione uma opção ")

            if(option == '1'):
                cls.show_next_launch()
                continue
            elif(option == '2'):
                cls.show_latest_launch()
                continue
            elif(option == '3'):
                cls.show_upcoming_launch()
                continue
            elif(option == '4'):
                cls.show_past_launch()
                continue
            elif(option == '5'):
                break
            else:
                print("\n\n")
                print("Por favor, escolha uma opção válida")

        print("\n\n")
        print("Obrigado por usar o Space X Journal!")
        print("---------------- =D --------------------")
        print("Source Code: https://github.com/BRZangado/SpaceXJournal")
        print("Desenvolvido por Bruno Rodrigues Santos")
        print("E-mail: bruesmanbruesman@hotmail.com")
        print("Github: https://github.com/BRZangado")

    @classmethod
    def print_launch(cls, launch):
        print("\n")
        print('---------------------------------')
        print(launch.get_info())
        print(launch.rocket.get_info())
        print(launch.launch_site.get_info())

    @classmethod
    def show_upcoming_launch(cls):
        launches = cls.db.get_upcoming_launches()
        for launch in launches:
            cls.print_launch(launch)

    @classmethod
    def show_past_launch(cls):
        launches = cls.db.get_past_launches()
        for launch in launches:
            cls.print_launch(launch)

    @classmethod
    def show_next_launch(cls):
        launch = cls.db.get_next_launch()
        cls.print_launch(launch)

    @classmethod
    def show_latest_launch(cls):
        launch = cls.db.get_latest_launch()
        cls.print_launch(launch)
