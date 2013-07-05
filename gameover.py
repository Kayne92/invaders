import pygame
from WorldObject import *
from constants import *

class Winner(WorldObject):
    def __init__(self, controller):
        super(Winner, self).__init__('winner.gif', 1, (SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 - 150))
        self.timer = 100
        self.controller = controller

    def update(self):
        super(Winner, self).update()
        self.timer -= 1
        if self.timer == 0:
            self.contoller.running = False