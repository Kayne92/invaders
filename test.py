import unittest
from invaders_main import *


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.alien = Alien(self.game, 305, 350)
        self.alien.update()
        self.in_world_bullet = PlayerBullet(self.game, (310, 350))
        self.out_of_world_bullet = PlayerBullet(self.game, (300, -10))
        self.out_of_world_enemy_bullet = EnemyBullet(self.game, (300, 5000))

        self.player = Player(self.game)
        self.game.player = self.player

        self.enemy_bullet = EnemyBullet(self.game, (320, 520))

        self.game.addWorldObject(self.out_of_world_bullet)
        self.game.addWorldObject(self.enemy_bullet)
        self.game.addWorldObject(self.in_world_bullet)
        self.game.addWorldObject(self.alien)

        self.out_of_world_bullet.update()
        self.enemy_bullet.update()

        self.game.check_collision(self.in_world_bullet)
        self.game.check_collision(self.player)

    def test_bullet_out_of_world(self):
        self.assertNotIn(self.out_of_world_bullet, self.game.objects)

    def test_alien_dies_when_hit(self):
        self.assertNotIn(self.alien, self.game.objects)

    def test_player_lives(self):
        self.assertEqual(len(self.player.lives), self.player.lives_count - 1)

    def test_score(self):
        self.assertEqual(self.game.score, 75)

    def test_bullet_exists(self):
        self.assertNotIn(self.in_world_bullet, self.game.objects)

    def test_enemy_bullet_exists(self):
        self.assertNotIn(self.out_of_world_enemy_bullet, self.game.objects)


if __name__ == '__main__':
    unittest.main()