from menu import Menu
from TCPClient import CommandSender
from robot import Robot
import pygame
from tkinter import messagebox
from frame import *
from pygame.locals import *
import lib.common_pb2 as comm
import time
  
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((520,680))
    pygame.display.set_caption("VSSS")
    yellow_sprites, blue_sprites = create_sprites()
    clock = pygame.time.Clock()

    teclas=[]

    t_ini=time.time()

    funcionando=True
    while funcionando:
        clock.tick(60)
        screen.fill((0,0,0))

        t_ciclo=time.time()-t_ini
        t_ini=time.time()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                funcionando=False
                client.send_command("c")


            elif event.type == pygame.KEYDOWN:
                key=check_key(event.key)

                if key not in teclas and key!='p':
                    teclas.append(key)
            elif event.type == pygame.KEYUP:
                key=check_key(event.key)

                if key in teclas:
                    teclas.remove(key)

        try:
            t1 = time.time()
            frame = get_package()
            t_parte = time.time() - t1

            index = 0
            for robot in blue_sprites:
                robot.locate(frame.robots_blue[index].x,frame.robots_blue[index].y,frame.robots_blue[index].orientation)
                index += 1

            index2 = 0
            for robot in yellow_sprites:
                robot.locate(frame.robots_yellow[index2].x,frame.robots_yellow[index2].y,frame.robots_yellow[index2].orientation)
                index2 += 1

            if len(teclas) == 1:
                envio = teclas[0]
            elif len(teclas) == 2:
                teclas.sort()

                if teclas[0] == 'a' and teclas[1] == 'w':
                    envio = 'q'
                elif teclas[0] == 'd' and teclas[1] == 'w':
                    envio = 'e'
                elif teclas[0] == 'a' and teclas[1] == 's':
                    envio = 'z'
                elif teclas[0] == 'd' and teclas[1] == 's':
                    envio = 'x'
                else:
                    envio = 'p'
            else:
                envio = 'p'

            client.send_command(envio)

        except:
            funcionando=False
            messagebox.showerror(title="Error", message="Conexão encerrada!")

        yellow_sprites.draw(screen)
        blue_sprites.draw(screen)
        pygame.display.flip()

        print(format(t_ciclo, ".5f"), end=" ")
        print(format(t_parte, ".5f"), end=" ")

    pygame.quit()

def check_key(key):
    if key == pygame.K_a or key == pygame.K_LEFT:
        return 'a'
    elif key == pygame.K_w or key == pygame.K_UP:
        return 'w'
    elif key == pygame.K_d or key == pygame.K_RIGHT:
        return 'd'
    elif key == pygame.K_s or key == pygame.K_DOWN:
        return 's'
    else:
        return 'p'


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

    print(frame.robots_blue[0].x, frame.robots_blue[0].y, frame.robots_blue[0].orientation)

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
