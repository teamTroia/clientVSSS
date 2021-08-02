import pygame
from pygame.locals import *
import lib.common_pb2 as comm

class Screen():
    def __init__(self, connection):
        pygame.init()
        self.connection = connection
        self.screen = pygame.display.set_mode((520,680))
        pygame.display.set_caption("VSSS")
        self.all_sprites = self.create_sprites()

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
            
    def get_package(self):
        data = self.connection.recv(1024)
        frame = comm.Frame.FromString(data)
        return frame

    def create_sprites(self):
        group = pygame.sprite.Group()

        return group

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = self.load_sprites()
        self.image = self.sprites[0]
    
    def load_sprites(self):
        sprites = []
        sprites.append(pygame.image.load("robo.png"))
        return sprites

    def set_position(self):
        pass
