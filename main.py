from menu import Menu
from TCPClient import CommandSender
from robot import Robot
import pygame
from pygame.locals import *
import lib.common_pb2 as comm
  
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((520,680))
    pygame.display.set_caption("VSSS")
    yellow_sprites, blue_sprites = create_sprites()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()

        try:
            frame = get_package()
        except:
            pass
        
        index = 0
        for robot in blue_sprites:
            robot.locate(frame.robots_blue[index].x,frame.robots_blue[index].y,frame.robots_blue[index].orientation)
            index += 1

        index2 = 0
        for robot in yellow_sprites:
            robot.locate(frame.robots_yellow[index2].x,frame.robots_yellow[index2].y,frame.robots_yellow[index2].orientation)
            index2 += 1

        yellow_sprites.draw(screen)
        blue_sprites.draw(screen)
        pygame.display.flip()

def create_sprites():
        group_yellow = pygame.sprite.Group()
        group_blue = pygame.sprite.Group()

        for i in range(3):
            group_yellow.add(Robot(1,i))
            group_blue.add(Robot(0,i))

        return group_yellow, group_blue

def get_package():
    global client
    data = client.receive_command(1024)
    try:
        frame = comm.Frame.FromString(data)
    except:
        raise NameError("NO DATA")
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
        print("ocupado")
    else:
        print("conectado")
        menu.hide()
        run_game()
        



menu = Menu(start_com)
menu.run()
client = None