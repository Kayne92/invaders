import pygame
from constants import *
from WorldObject import *
from bullet import *
from explosion import *


class Alien(WorldObject):
    speed = 3
    direction = 1

    def __init__(self, controller, xpos, level, *groups):
        super(Alien, self).__init__('enemy ships.png', 8, (xpos, 70))
        self.level = level
        self.controller = controller
        self.alien_level = 0
        self.alien_direction = 1
        self.cnt = 0
        self.score = 75

    def update(self):
        super(Alien, self).update()
        self.frame += 1
        if self.frame >= self.last_frame:
            self.frame = 0
        self.rect.x += self.speed * self.alien_direction  # self.direction
        self.rect.y = self.alien_level * self.image_size[1] + self.level

        if self.controller.alien_shoot_timer >= self.controller.alien_shoot_frequency:
            self.shoot()  # no pun intended

        if(self.rect.x > (SCREEN_WIDTH - self.image_size[1]) or self.rect.x < 0):
            self.controller.change_direction()

    def shoot(self):
        gun_pos = (self.rect.x + self.image_size[0] // 2, self.rect.y + self.image_size[1])
        self.controller.addWorldObject(EnemyBullet(self.controller, gun_pos))
        self.controller.alien_shoot_timer = 0

    def kill(self):
        super(Alien, self).kill()
        #self.controller.score += self.score - self.alien_level