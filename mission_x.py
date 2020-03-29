'''
Author: Aidan Good
Based on Python Crash Course project by Eric Matthes

Main file that will initialize and handle running the game
'''
import sys
import pygame
import random
from settings import Settings
from ship import Ship
from rocket import Rocket
from alien import Alien

class Adventure:
    """Overarching class to manage assets and behaviors"""

    def __init__( self ):
        """Start up the game window and intialize game resources"""
        
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption( "Mission X" )

        self.ship = Ship( self )
        self.rockets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def start_game( self ):
        """Begin main loop"""
        while True:
            self.check_inputs()
            self.ship.moving()
            self.rocket_update()
            self.create_alien()
            self.alien_update()
            self.draw_screen()

    def alien_update( self ):
        self.aliens.update()

        # Remove aliens that reach right end of screen
        for alien in self.aliens.copy():
            if alien.rect.right <= 0:
                self.aliens.remove( alien )

        # Check for collisions with player ship
        if pygame.sprite.spritecollideany( self.ship, self.aliens ):
            

    def create_alien( self ):
        if len( self.aliens ) < self.settings.num_aliens:
            if random.random() < self.settings.alien_rate:
                newAlien = Alien( self )
                self.aliens.add( newAlien )
        
    def rocket_update( self ):
        """Handles moving rockets"""
        
        self.rockets.update()
        
        # Limit # of rockets on screen
        for rocket in self.rockets.copy():
            if rocket.rect.left >= self.screen.get_rect().width:
                self.rockets.remove( rocket )

        # Check for rocket colisions with aliens and asteroids
        alien_collisions = pygame.sprite.groupcollide(
            self.rockets, self.aliens, True, True )

        #ADD asteroids

        

    
    def fire_rocket( self ):
        """Handles firing and tracking # of rockets"""
        if len( self.rockets ) < self.settings.num_rockets:
            newRocket = Rocket( self )
            self.rockets.add( newRocket )
            

    def check_inputs( self ):
        """Watch for keyboard commands and respond"""
            
        for event in pygame.event.get():
            # Quit if game is exited
            self.userquit_game( event )
                
            # Check for keypress
            if event.type == pygame.KEYDOWN:
                self.keydown_check( event )

            # Check for user releasing keys
            elif event.type == pygame.KEYUP:
                self.keyup_check( event )

    def userquit_game( self, event ):
        """Manages user quitting the game"""
        
        # Quit if game is exited
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    def keydown_check( self, event ):
        """Handles the user pressing a key"""
        
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
            
    def keyup_check( self, event ):
        """Handles the user releasing key"""
        
        # Stop upward movement when user stops pressing key down
        if event.key == pygame.K_LEFT or event.key == pygame.K_UP:
            self.ship.moving_up = False
            
        # Stop downward movement when user stops pressing key down
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def draw_screen( self ):
        """Handles updating the display"""
        
        self.screen.fill( self.settings.bg_color )
        self.rockets.draw(self.screen)
        self.ship.draw()
        self.aliens.draw(self.screen)
            
        pygame.display.flip()

if __name__ == '__main__':
    a = Adventure()
    a.start_game()
