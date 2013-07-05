import pygame
from constants import *
from WorldObject import *

class Player(WorldObject):

    speed = 6
    can_shoot = True

    def __init__(self, controller, *groups):

        super(Player, self).__init__('spaceship.png', (320, PLAYER_YPOS), groups)
        self.controller = controller

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            if self.rect.x < SCREEN_WIDTH - (self.image.get_size()[0] + self.speed):
                self.rect.x += self.speed
        if key[pygame.K_SPACE]:
            if(not self.can_shoot):
                return
            pos = (self.rect.x + self.image_size[0] // 2, self.rect.y)
            self.controller.addBullet(pos)
            self.can_shoot = False