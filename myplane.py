import pygame
import os

class Myplane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load('images/me1.png').convert_alpha()
        self.image2 = pygame.image.load('images/me2.png').convert_alpha()
        self.destory_images=[]
        self.destory_images.extend([
            pygame.image.load('images/me_destroy_1.png').convert_alpha(),
            pygame.image.load('images/me_destroy_2.png').convert_alpha(),
            pygame.image.load('images/me_destroy_3.png').convert_alpha(),
            pygame.image.load('images/me_destroy_4.png').convert_alpha()]
            )
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0] , bg_size[1]
        self.rect.left,self.rect.top = (self.width-self.rect.width)//2,\
                                       (self.height-self.rect.height-15)
        self.speed = 10
        self.destory = False
        self.mask = pygame.mask.from_surface(self.image1)
    def moveup(self):
        if self.rect.top>0:
            self.rect.top -=self.speed
        else:
            self.rect.top = 0
    def movedown(self):
        if self.rect.bottom <self.height-15:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height-15
    def moveleft(self):
        if self.rect.left >0:
            self.rect.left -=self.speed
        else:
            self.rect.left = 0
    def moveright(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
    def reset(self):
        self.rect.left,self.rect.top = (self.width-self.rect.width)//2,\
                                       (self.height-self.rect.height-15)
        self.destory = False

