import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        #create a bullet rect at (0, 0) and then set correct posiiton.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet's posiiton as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        #Update the decimla position of the bullet.
        self.y -= self.settings.bullet_speed
        #update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet onto screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
