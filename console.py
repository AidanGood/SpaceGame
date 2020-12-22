'''
Author: Aidan Good
'''
import pygame

class Console:
    """Bottom console showing stats such as rockets remaining, lives, remaining, etc."""

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.rect = pygame.Rect(0, game.settings.screen_height - 190, game.settings.screen_width, 190)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color('gray30'), self.rect)