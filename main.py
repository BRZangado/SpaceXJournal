from controllers.DataController import DataController

db = DataController()
db.init_database()

def show_upcoming_launch():
    print("")
    launches = db.get_upcoming_launches()
    for launch in launches:
        print(launch.get_info())
        print(launch.rocket.get_info())
        print(launch.launch_site.get_info())

def show_past_launch():
    print("")
    launches = db.get_past_launches()
    for launch in launches:
        print(launch.get_info())
        print(launch.rocket.get_info())
        print(launch.launch_site.get_info())

def show_next_launch():
    print("")
    launch = db.get_next_launch()
    print(launch.get_info())
    print(launch.rocket.get_info())
    print(launch.launch_site.get_info())

def show_latest_launch():
    print("")
    launch = db.get_latest_launch()
    print(launch.get_info())
    print(launch.rocket.get_info())
    print(launch.launch_site.get_info())

if __name__ == '__main__':

    print("")
    print("")
    print(" ----- Bem vindo ao Space X Journal -----")
    print(" Confira os dados dos lançamentos da SpaceX")

    while True:

        print("")
        print("")
        print("Selecione uma opção:")
        print("(1) Próximo lançamento")
        print("(2) Último lançamento")
        print("(3) Próximos lançamentos")
        print("(4) Últimos lançamentos")
        print("(5) Sair")

        option = input()

        if(option == '1'):
            show_next_launch()
            continue
        elif(option == '2'):
            show_latest_launch()
            continue
        elif(option == '3'):
            show_upcoming_launch()
            continue
        elif(option == '4'):
            show_past_launch()
            continue
        elif(option == '5'):
            break
        else:
            print("")
            print("")
            print("Por favor, escolha uma opção válida")
    
    print("")
    print("")
    print("Obrigado por usar o Space X Journal!")
    print("---------------- =D --------------------")
    print("Source Code: https://github.com/BRZangado/SpaceXJournal")
    print("Desenvolvido por Bruno Rodrigues Santos")
    print("E-mail: bruesmanbruesman@hotmail.com")
    print("Github: https://github.com/BRZangado")