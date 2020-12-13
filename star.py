'''
Author: Aidan Good
'''
import pygame
from pygame.rect import Rect
import random
from pygame.sprite import Sprite


class Star(Sprite):
    """The stars that move in the background"""

    def __init__(self, game):
        """Create the star and set position randomly along y-axis"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.velocity = self.settings.star_velocity

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Place stars randomly on right side of screen
        self.rect.x = game.settings.screen_width
        self.rect.y = random.randint(0, game.settings.screen_height - 200)

        self.x = float(self.rect.x)

    def update(self):
        """Manages moving stars across the screen"""
        self.x -= self.velocity
        self.rect.x = self.x