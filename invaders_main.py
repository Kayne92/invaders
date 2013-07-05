import pygame
from bullet import *
from player import Player
from alien import Alien

class Game:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    sprites = pygame.sprite.Group()
    objects = []

    def __init__(self):
        pygame.init()
        self.background = pygame.image.load('background.jpg')
        for level in range(4):
            for alien_xpos in range(15):
                self.addWorldObject(Alien(self, alien_xpos * 40, level * 32))
        self.player = Player(self)
        self.addWorldObject(self.player)
        self.direction_flag = False
        self.alien_direction = 1
        self.alien_level = 0
        self.alien_shoot_frequency = 600
        self.alien_shoot_timer = 0

    def main(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            #self.sprite.update(self.t)

            for obj in self.objects:
                self.alien_shoot_timer += 1
                obj.update()
                self.check_collision(obj)

            self.updateAlienDirectionAndLevel()

            #self.sprites.draw(screen)
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
                            obj1.kill()
                            obj2.kill()

                    if(obj1.__class__ == Player):
                        if(obj2.__class__ == Alien or obj2.__class__ == EnemyBullet):
                            pygame.time.wait(1000)
                            self.running = False

    def addWorldObject(self, obj):
        self.objects.append(obj)

    def addBullet(self, pos):
        self.addWorldObject(PlayerBullet(self, pos))

    def killObject(self, obj):
        if(self.objects.__contains__(obj)):
            self.objects.remove(obj)

    def change_direction(self):
        self.direction_flag = True

if __name__ == '__main__':
    Game().main()
