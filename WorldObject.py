import pygame

class WorldObject(pygame.sprite.Sprite):

    def __init__(self, sprite, pos, *groups):
        super(WorldObject, self).__init__(*groups)
        self.image = pygame.image.load(sprite)
        self.image_size = self.image.get_size()
        self.rect = pygame.rect.Rect(pos, self.image_size)
        self.sprites = groups