'''
Author: Aidan Good
Based on Python Crash Course project by Eric Matthes
'''
import pygame

class Settings:
    """Class to manage game settings"""
    def __init__(self):
        # Display settings
        self.screen_width = ( 1200 )
        self.screen_height = ( 800 )
        self.bg_color = ( 230, 230, 230 )
        # Ship settings
        self.ship_speed = 4
        self.num_lives = 3
        # Rocket settings
        self.rocket_velocity = 0.75
        self.rocket_acceleration = 0.1
        self.rocket_width = 3
        self.rocket_height = 15
        self.rocket_color = ( 60, 60, 60 )
        self.num_rockets = 5
        # Alien settings
        self.alien_velocity = 2
        self.alien_rate = 0.01 # anything below 0.05 seems good
        self.num_aliens = 6
        
