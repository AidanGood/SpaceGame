'''
Author: Aidan Good
'''
import pygame.font


class Button:
    def __init__(self, game, message):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # Button properties
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_message(message)

    def prep_message(self, message):
        """ Make the message able to appear on the screen """
        self.msg_image = self.font.render(message, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button and then the message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
