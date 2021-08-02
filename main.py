from menu import Menu
from TCPClient import CommandSender
from tela import Screen

def start_com(addr, team, robot):
    global client, menu
    ip, port = addr.split(":")
    port = int(port)
    robot_id = robot
    team_id = 0
    if(team == "AMARELO"):
        team_id = 1

    client = CommandSender(ip, port)
    client.send_command(str(team_id)+str(robot_id))

    sucess = int(client.receive_command(1)[0])-48
    if(not(sucess)):
        print("ocupado")
    else:
        print("conectado")
        menu.hide()
        screen = Screen()
        ##screen.run()
        



menu = Menu(start_com)
menu.run()
client = None