import pygame

from button import Button

from config import *
from logger import Logger

import random

class UI:
    def __init__ (self, gamestate):
        self.logger = Logger()
        self.gamestate = gamestate
        self.screen = pygame.display.set_mode((800,600))
        self.font = pygame.font.Font(None, 16)
        self.buttons = []
        self.init_buttons()
        print(f"UI > CONSTRUCTOR: Default button list is: {self.buttons}.")

    def init_buttons(self):
        self.stats_button = Button(200,200,200,50,"Statistics",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('main'))
        self.vocab_button = Button(500,200,200,50,"Vocabulary",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))

    def handle_event(self, event): 
        for button in self.buttons:
            button.handle_event(event)

    # Define relevant UI buttons and bind actions from the gamestate
    def update(self):
        if self.gamestate.current_state == 'main':
            self.buttons = [self.stats_button, self.vocab_button]
            pass

    def render(self):
        if self.gamestate.current_state == 'main':
            for button in self.buttons:
                button.draw(self.screen)
        if self.gamestate.current_state == 'vocab':
            for button in self.buttons:
                button.draw(self.screen)


        pygame.display.update() # Cast updates to the display