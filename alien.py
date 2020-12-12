'''
Author: Aidan Good
Based on Python Crash Course project by Eric Matthes
'''
import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """Class to handle alien ships"""

    def __init__(self, game):
        """Create ship and make start position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.velocity = self.settings.alien_velocity

        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Place alien randomly on right side of screen
        self.rect.x = game.settings.screen_width
        self.rect.y = random.randint(0, game.settings.screen_height - 200)

        self.x = float(self.rect.x)

    def update(self):
        """Manages moving alien ships across the screen"""
        self.x -= self.velocity
        self.rect.x = self.x
