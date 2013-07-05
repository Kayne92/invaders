import pygame
from constants import *
from WorldObject import *

class Player(WorldObject):

    def __init__(self, controller, *groups):

        super(Player, self).__init__('ship.png', 5, (320, PLAYER_YPOS))
        self.controller = controller
        self.speed = 7
        self.reload_time = 4
        self.shoot_timer = 0
        self.cnt = 0

    def update(self):
        super(Player, self).update()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if(self.cnt > 0 - self.last_frame // 2 - 2):
                self.cnt -= 1
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif key[pygame.K_RIGHT]:
            if(self.cnt < self.last_frame):
                self.cnt += 1
            if self.rect.x < SCREEN_WIDTH - (self.image.get_size()[0] + self.speed):
                self.rect.x += self.speed
        else:
            if(self.cnt > 0):
                self.cnt -= 1
            if(self.cnt < 0):
                self.cnt += 1

        if key[pygame.K_SPACE]:
            if self.shoot_timer > 0:
                self.shoot_timer -= 1
            else:
                pos = (self.rect.x + self.image_size[0] // 2, self.rect.y)
                self.controller.addBullet(pos)
                self.shoot_timer = self.reload_time
        self.frame = 2 + self.cnt // 2
        self.controller.screen.blit(self.images[self.frame], self.rect)
