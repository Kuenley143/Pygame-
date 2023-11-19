import unittest
import pygame
class PygameTest(unittest.TestCase):
   def setUp(self):
       pygame.init()

   def test_screen_size(self):
       screen = pygame.display.set_mode((800, 300))
       self.assertEqual(screen.get_width(), 800)
       self.assertEqual(screen.get_height(), 300)
   

   class TestCastle(unittest.TestCase):
    def setUp(self):
       self.castle = castle(image100, x, y, scale)
       self.bullet_group = pygame.sprite.Group()

    def test_shoot(self):
       # Test if a bullet is created when the mouse button is pressed
       pygame.mouse.set_pos((x, y))
       pygame.mouse.set_pressed([1])
       self.castle.shoot()
       self.assertEqual(len(self.bullet_group), 1)

       # Test if the bullet is not created when the mouse button is not pressed
       pygame.mouse.set_pressed([0])
       self.castle.shoot()
       self.assertEqual(len(self.bullet_group), 1)
if __name__ == '__main__':
   unittest.main()

