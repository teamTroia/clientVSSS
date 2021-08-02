import pygame
from pygame.locals import *
import lib.common_pb2 as comm

class Screen():
    def __init__(self, connection):
        pygame.init()
        self.connection = connection
        self.screen = pygame.display.set_mode((520,680))
        pygame.display.set_caption("VSSS")
        self.yellow_sprites, blue_sprites = self.create_sprites()

    def run(self):
        while True:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if(event.type == QUIT):
                    pygame.quit()
                if(event.type == KEYDOWN):
                    if(event.key == K_LEFT):
                        robo.rotate(90)
                    if(event.key == K_RIGHT):
                        robo.rotate(-90)

            frame = self.get_package()

        for robot, index in enumerate(frame.robots_blue):
            self.blue_sprites[index].locate(robot.x,robot.y,robot.orientation)
        
        for robot, index in enumerate(frame.robots_yellow):
            self.yellow_sprites[index].locate(robot.x,robot.y,robot.orientation)
        
        self.yellow_sprites.draw(self.screen)
        self.blue_sprites.draw(self.screen)
            
    def get_package(self):
        data = self.connection.recv(1024)
        frame = comm.Frame.FromString(data)
        return frame

    def create_sprites(self):
        group_yellow = pygame.sprite.Group()
        group_blue = pygame.sprite.Group()

        for i in range(3):
            group_yellow.add(Robot(1,i))
            group_blue.add(Robot(0,i))

        return group_yellow, group_blue

class Robot(pygame.sprite.Sprite):
    def __init__(self, isYellow, id):
        self.path = "sprites/azul/"
        self.name = 'azul'+str(id)
        if(isYellow):
            self.path = "sprites/amarelo/"
            self.name = 'amarelo'+str(id)

        pygame.sprite.Sprite.__init__(self)
        self.sprites = self.load_sprites()
        self.image = self.sprites[0]
    
    def load_sprites(self):
        sprites = []
        sprites.append(pygame.image.load(f"{self.path}{self.name}+-0.png"))
        sprites.append(pygame.image.load(f"{self.path}{self.name}+-18.png"))
        sprites.append(pygame.image.load(f"{self.path}{self.name}+-36.png"))
        sprites.append(pygame.image.load(f"{self.path}{self.name}+-54.png"))
        sprites.append(pygame.image.load(f"{self.path}{self.name}+-72.png"))
        return sprites

    def locate(self,x,y,angle):
        self.rotate(angle)
        self.set_position(x, y)

    def set_position(self, x,y):
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def rotate(self, angle):
        pass
