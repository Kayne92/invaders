import pygame
from constants import *
from WorldObject import *

class Bullet(WorldObject):
    def __init__(self, image, speed, controller, pos, *groups):
        super(Bullet, self).__init__(image, pos, *groups)
        self.rect.x -= self.image_size[0] // 2
        self.controller = controller
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if(self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT):
            self.controller.allowShooting()
            self.controller.killObject(self)
            self.kill()


class PlayerBullet(Bullet):

    def __init__(self, controller, pos, *groups):
        super(PlayerBullet, self).__init__('bullet.png', -20, controller, pos, *groups)

    def kill(self):
        super(PlayerBullet, self).kill()
        self.controller.allowShooting()
