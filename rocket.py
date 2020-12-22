'''
Author: Aidan Good
'''
import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    """Class to manage rockets fired from the players ship"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.rocket_color

        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright

        self.x = float(self.rect.x)
        self.velocity = self.settings.rocket_velocity

    def draw(self):
        """Draws rockets at ship's position"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Manages moving rockets across the screen"""
        self.x += self.velocity
        # Rocket accelerates as it goes across the screen
        if self.velocity < 10:
            self.velocity += self.settings.rocket_acceleration
        self.rect.x = self.x
