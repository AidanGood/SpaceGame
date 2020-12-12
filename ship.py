'''
Author: Aidan Good
'''
import pygame


class Ship:
    """Class that manages the players ship"""

    def __init__(self, game):
        """Create the ship and it's attributes"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # Get ship image from the images folder
        self.image = pygame.image.load('images/player_ship.png')
        self.rect = self.image.get_rect()

        # Position the ship at the center-left side of the screen at start
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        """Draws ship at its current position"""

        self.screen.blit(self.image, self.rect)

    def moving(self):
        """Manages moving ship up and down based on flags"""

        if self.moving_up == True and self.rect.top - 3 > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down == True and self.rect.bottom + 3 < \
                self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center(self):
        """ Puts ship back at starting position """

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
