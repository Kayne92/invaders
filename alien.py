import pygame
from constants import *
from WorldObject import *

class Alien(WorldObject):
    speed = 5
    direction = 1

    def __init__(self, controller, xpos, level, *groups):
        super(Alien, self).__init__('invader.png', (xpos, 70), groups)
        self.level = level
        self.controller = controller
        self.alien_level = 0
        self.alien_direction = 1

    def update(self):
        self.rect.x += self.speed * self.alien_direction  # self.direction
        self.rect.y = self.alien_level * self.image_size[1] + self.level

        if(self.rect.x > (SCREEN_WIDTH - self.image_size[1]) or self.rect.x < 0):
            self.controller.change_direction()