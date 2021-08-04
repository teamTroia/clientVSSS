from menu import Menu
from TCPClient import CommandSender
from robot import Robot
import pygame
from tkinter import messagebox
from frame import *
from pygame.locals import *
import lib.common_pb2 as comm
  
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((520,680))
    pygame.display.set_caption("VSSS")
    yellow_sprites, blue_sprites = create_sprites()
    clock = pygame.time.Clock()
    
    funcionando=True
    while funcionando:
        client.send_command("p")

        clock.tick(60)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                funcionando=False
                client.send_command("c")

        try:
            frame = get_package()

            index = 0
            for robot in blue_sprites:
                robot.locate(frame.robots_blue[index].x,frame.robots_blue[index].y,frame.robots_blue[index].orientation)
                index += 1

            index2 = 0
            for robot in yellow_sprites:
                robot.locate(frame.robots_yellow[index2].x,frame.robots_yellow[index2].y,frame.robots_yellow[index2].orientation)
                index2 += 1
        except:
            funcionando=False
            messagebox.showerror(title="Error", message="Conexão encerrada!")

        yellow_sprites.draw(screen)
        blue_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

def create_sprites():
        group_yellow = pygame.sprite.Group()
        group_blue = pygame.sprite.Group()

        for i in range(3):
            group_yellow.add(Robot(1,i))
            group_blue.add(Robot(0,i))

        return group_yellow, group_blue

def get_package():
    global client
    data = client.receive_command(80)
    data = data.decode('utf-8')

    frame=Frame()

    for i in range(3):
        frame.robots_blue[i].x = float(data[i * 12 :i * 12 + 4])
        frame.robots_blue[i].y = float(data[i * 12 + 4 :i * 12 + 8])
        frame.robots_blue[i].orientation = float(data[i * 12 + 8 :i * 12 + 12])

        frame.robots_yellow[i].x = float(data[i * 12 + 36 :i * 12 + 40])
        frame.robots_yellow[i].y = float(data[i * 12 + 40 :i * 12 + 44])
        frame.robots_yellow[i].orientation = float(data[i * 12 + 44 :i * 12 + 48])

    frame.ball.x = float(data[72:76])
    frame.ball.y = float(data[76:80])

    print(frame.robots_blue[0].x, frame.robots_blue[0].y)

    return frame
    
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
        messagebox.showerror(title="Error", message="Robô ocupado!")
    else:
        menu.hide()
        run_game()
        menu.show()
        



menu = Menu(start_com)
menu.run()
client = None
