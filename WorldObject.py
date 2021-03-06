import pygame
import os
from constants import *

class WorldObject(pygame.sprite.Sprite):

    def load_sliced_sprites(self, filename, frames):

        images = []
        master_image = pygame.image.load(os.path.join('resources', filename)).convert_alpha()
        master_width, master_height = master_image.get_size()
        frame_width = master_width // frames
        for i in range(master_width // frame_width):
            images.append(master_image.subsurface((i * frame_width, 0, frame_width, master_height)))
        return images

    def __init__(self, sprite, frames, pos):
        #uper(WorldObject, self).__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.images = self.load_sliced_sprites(sprite, frames)
        self.image = self.images[0]
        self.image_size = self.image.get_size()
        self.rect = pygame.rect.Rect(pos, self.image_size)
        self.frame = 0
        self.last_frame = frames

    def update(self):
        self.controller.screen.blit(self.images[self.frame], self.rect)

    def kill(self):
        super(WorldObject, self).kill()
        self.controller.killObject(self)
        self.alive = False

class Coin(WorldObject):
    def __init__(self, controller, pos):
        super(Coin, self).__init__('coin.png', 6, pos)
        self.speed = 7
        self.controller = controller
        self.controller.addWorldObject(self)

    def update(self):
        super(Coin, self).update()
        self.rect.y += self.speed
        self.frame += 1
        if(self.frame >= self.last_frame):
            self.frame = 0
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()
