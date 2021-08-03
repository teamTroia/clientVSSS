import pygame
from pygame.locals import *
import lib.common_pb2 as comm

class Robot(pygame.sprite.Sprite):
    def __init__(self, isYellow, id):
        self.path = "sprites/azul/"
        self.name = "azul"+str(id+1)
        if(isYellow):
            self.path = "sprites/amarelo/"
            self.name = "amarelo"+str(id+1)

        pygame.sprite.Sprite.__init__(self)
        self.sprites = self.load_sprites()
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
    
    def load_sprites(self): 
        sprites = []
        sprites.append(pygame.image.load(self.path + self.name + "-0.png"))
        sprites.append(pygame.image.load(self.path + self.name + "-18.png"))
        sprites.append(pygame.image.load(self.path + self.name + "-36.png"))
        sprites.append(pygame.image.load(self.path + self.name + "-54.png"))
        sprites.append(pygame.image.load(self.path + self.name + "-72.png"))
        return sprites

    def locate(self,x,y,angle):
        #self.rotate(angle)
        self.set_position(x, y)

    def set_position(self, y,x):
        x = (x+0.65)*400
        y = (y+0.85)*400
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def rotate(self, angle):
        pass
