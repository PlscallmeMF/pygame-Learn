import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.img)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False


    def reset4(self,position):
        self.rect.left, self.rect.top = position
        self.active = True
