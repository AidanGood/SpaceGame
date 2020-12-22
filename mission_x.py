'''
Author: Aidan Good

Main file that will initialize and handle running the game
'''
import sys
import pygame
import random
import time

from settings import Settings
from game_stats import GameStats
from ship import Ship
from rocket import Rocket
from alien import Alien
from button import Button
from star import Star
from console import Console


class Adventure:
    """ Overarching class to manage game logic and behaviors """

    def __init__(self):
        """ Start up the game window and initialize game resources """

        pygame.init()

        # Get game settings
        self.settings = Settings()

        # Set up the display
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Mission X")
        self.console = Console(self)

        # Start storing game statistics
        self.stats = GameStats(self)

        # Attach appropriate groups to respective variables
        self.ship = Ship(self)
        self.rockets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        # Make play button
        self.play_button = Button(self, 'Play')

    def start_game(self):
        """ Begin game logic loop """

        self.create_background_stars()

        while True:
            self.check_inputs()

            if self.stats.game_active:
                self.ship.moving()
                self.rocket_update()
                self.create_alien()
                self.alien_update()
                self.create_stars()
                self.star_update()

            self.draw_screen()

    def ship_impact(self):
        """ When the ship gets hit by an object """

        # Remove 1 life
        if self.stats.lives_left > 0:

            self.stats.lives_left -= 1
            # Remove all on-screen objects
            self.aliens.empty()
            self.rockets.empty()
            # Move ship back to starting position
            self.ship.center()
            # Pause the game
            time.sleep(0.5)

        else:
            self.stats.game_active = False

    def alien_update(self):
        """ Handle interactions with alien ships """

        self.aliens.update()

        # Remove aliens that reach right end of screen
        for alien in self.aliens.copy():
            if alien.rect.right <= 0:
                self.aliens.remove(alien)

        # Check for collisions with player ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_impact()

    def star_update(self):
        """Make the stars move across the screen"""

        self.stars.update()

        # Remove stars that reach right end of screen
        for star in self.stars.copy():
            if star.rect.right <= 0:
                self.stars.remove(star)

    def create_alien(self):
        """Create aliens randomly and ensure that no more than the max appear on screen at once"""

        if len(self.aliens) < self.settings.num_aliens:
            if random.random() < self.settings.alien_rate:
                newAlien = Alien(self)
                self.aliens.add(newAlien)

    def create_stars(self):
        """Create stars randomly"""

        if random.random() < self.settings.star_rate:
            newStar = Star(self)
            self.stars.add(newStar)

    def create_background_stars(self):
        for i in range(20):
            newStar = Star(self, 1)
            self.stars.add(newStar)

    def rocket_update(self):
        """ Handles moving rockets """

        self.rockets.update()

        # Limit # of rockets on screen
        for rocket in self.rockets.copy():
            if rocket.rect.left >= self.screen.get_rect().width:
                self.rockets.remove(rocket)

        # Check for rocket collisions with aliens and asteroids
        alien_collisions = pygame.sprite.groupcollide(
            self.rockets, self.aliens, True, True)

        '''TODO: Add asteroids'''

    def fire_rocket(self):
        """ Handles firing and tracking # of rockets on screen """
        if len(self.rockets) < self.settings.num_rockets:
            newRocket = Rocket(self)
            self.rockets.add(newRocket)

    def check_inputs(self):
        """ Watch for keyboard commands and respond """

        for event in pygame.event.get():
            # Quit if game is exited
            self.userquit_game(event)

            # Check for keypress
            if event.type == pygame.KEYDOWN:
                self.keydown_check(event)

            # Check for user releasing keys
            elif event.type == pygame.KEYUP:
                self.keyup_check(event)

    def userquit_game(self, event):
        """ Manages user quitting the game """

        # Quit if game is exited
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def keydown_check(self, event):
        """ Handles keypresses """

        # Upward movement inputs - up or left arrow key 
        if event.key == pygame.K_LEFT or event.key == pygame.K_UP:
            self.ship.moving_up = True

        # Downward movement inputs - right or down arrow key         
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        # Fire a rocket - spacebar
        elif event.key == pygame.K_SPACE:
            self.fire_rocket()

        # Exit game - 'Q' or 'esc' key
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    def keyup_check(self, event):
        """ Handles the user releasing key """

        # Stop upward movement when user stops pressing key down
        if event.key == pygame.K_LEFT or event.key == pygame.K_UP:
            self.ship.moving_up = False

        # Stop downward movement when user stops pressing key down
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def draw_screen(self):
        """ Handles updating the display """

        self.screen.fill(self.settings.bg_color)
        self.console.draw()
        self.stars.draw(self.screen)
        self.rockets.draw(self.screen)
        self.ship.draw()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    a = Adventure()
    a.start_game()
