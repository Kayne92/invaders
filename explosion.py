import pygame
from WorldObject import WorldObject


class Explosion(WorldObject):
    def __init__(self, controller, pos):
        super(Explosion, self).__init__('explosion.png', 17, pos)
        self.controller = controller
        #self.controller.addWorldObject(self, pos)

    def update(self):
        super(Explosion, self).update()
        self.frame += 1
        if(self.frame == self.last_frame):
            self.kill()

class SmallExplosion(WorldObject):
    def __init__(self, controller, pos):
        super(SmallExplosion, self).__init__('explosion2.png', 13, pos)
        self.controller = controller

    def update(self):
        super(SmallExplosion, self).update()
        self.frame += 1
        if(self.frame == self.last_frame):
            self.kill()