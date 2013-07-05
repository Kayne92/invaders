import pygame
import os

screen = pygame.display.set_mode((800, 600))


def load_sliced_sprites(self, filename, frames):

    images = []
    master_image = pygame.image.load(filename).convert_alpha()
    master_width, master_height = master_image.get_size()
    frame_width = master_width // frames
    for i in range(master_width // frame_width):
        images.append(master_image.subsurface((i * frame_width, 0, frame_width, master_height)))
    return images


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, pos, images, fps=10):
        pygame.sprite.Sprite.__init__(self)
        self._images = images
        self.rect = pygame.rect.Rect(pos, images[0].get_size())
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 2
        self._last_frame = len(self._images)
        self._first_frame = 0
        self.cnt = 0
        self.update()

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if(self.cnt < self._last_frame):
                self.cnt += 1
            self.rect.x += 3
        else:
            if(self.cnt > 0):
                self.cnt -= 1

        self._frame = 2 + self.cnt // 2
        screen.blit(self._images[self._frame], self.rect)


class Game:
    clock = pygame.time.Clock()
    background = pygame.image.load('background.jpg')
    running = True
    # sprites = pygame.sprite.Group()

    def main(self):

        self.images = load_sliced_sprites(self, 'ship.png', 5)
        self.sprite = AnimatedSprite((300, 560), self.images)
        self.t = 0
        while self.running:
            screen.blit(self.background, (0, 0))
            self.clock.tick(30)
            self.t += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.sprite.update()


            pygame.display.flip()

if __name__ == '__main__':
    Game().main()
