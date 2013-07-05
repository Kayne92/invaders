import pygame
from bullet import *
from player import Player
from alien import Alien
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Game:
    clock = pygame.time.Clock()
    running = True
    sprites = pygame.sprite.Group()
    objects = []

    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('background.jpg')
        for level in range(4):
            for alien_xpos in range(15):
                self.addWorldObject(Alien(self, alien_xpos * 40, level * 32, self.sprites))
        self.player = Player(self, self.sprites)
        self.addWorldObject(self.player)
        self.direction_flag = False
        self.alien_direction = 1
        self.alien_level = 0

    def main(self):
        while self.running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            for obj in self.objects:
                obj.update()
                self.check_collision(obj)

            self.updateAlienDirectionAndLevel()

            screen.blit(self.background, (0, 0))
            self.sprites.draw(screen)
            pygame.display.flip()

    def updateAlienDirectionAndLevel(self):
        for alien in self.objects:
            if(self.direction_flag and alien.__class__ == Alien):
                alien.alien_direction *= -1
                alien.alien_level += 1
        self.direction_flag = False

    def check_collision(self, obj1):
        for obj2 in self.objects:
            if obj1.__class__ != obj2.__class__:
                if obj1.rect.colliderect(obj2.rect):
                    if(obj1.__class__ == PlayerBullet):
                        if(obj2.__class__ != Player):
                            self.killObject(obj1)
                            self.killObject(obj2)

                    if(obj1.__class__ == Player):
                        if(obj2.__class__ == Alien):
                            pygame.time.wait(1000)
                            self.running = False

    def addWorldObject(self, obj):
        self.objects.append(obj)

    def addBullet(self, pos):
        self.addWorldObject(PlayerBullet(self, pos, self.sprites))

    def allowShooting(self):
        self.player.can_shoot = True

    def killObject(self, obj):
        if(self.objects.__contains__(obj)):
            self.objects.remove(obj)
        obj.kill()

    def change_direction(self):
        self.direction_flag = True

if __name__ == '__main__':
    Game().main()
