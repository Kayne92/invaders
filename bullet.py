import pygame
from constants import *
from WorldObject import *

class Bullet(WorldObject):
    def __init__(self, image, speed, controller, pos):
        super(Bullet, self).__init__(image, 1, pos)
        self.rect.x -= self.image_size[0] // 2
        self.controller = controller
        self.speed = speed

    def update(self):
        super(Bullet, self).update()
        self.rect.y += self.speed
        if(self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT):
            self.kill()


class PlayerBullet(Bullet):

    def __init__(self, controller, pos):
        super(PlayerBullet, self).__init__('bullet.png', -20, controller, pos)

    def kill(self):
        super(PlayerBullet, self).kill()

class EnemyBullet(Bullet):
    def __init__(self, controller, pos):
        super(EnemyBullet, self).__init__('bullet2.gif', 20, controller, pos)