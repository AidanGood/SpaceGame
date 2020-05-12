'''
Author: Aidan Good
Based on Python Crash Course project by Eric Matthes
'''

class GameStats:
    ''' Tracks changable statistics and settings during the game '''

    def __init__( self, game ):
        ''' Initialize statistics '''

        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats( self ):
        ''' Resets changed statistics when a new game is started '''
        self.lives_left = self.settings.life_limit
