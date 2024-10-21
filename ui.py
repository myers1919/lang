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
        self.font = pygame.font.Font(None, 24)
        self.buttons = []
        self.init_buttons()
        print(f"UI > CONSTRUCTOR: Default button list is: {self.buttons}.")

    def init_buttons(self):
        self.main_button = Button(10,10,200,50,"Main Menu",self.font,PINK,PINK_HOVER,lambda: self.gamestate.change_state('main'))
        self.stats_button = Button(200,200,200,50,"Statistics",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('stats'))
        self.vocab_button = Button(500,200,200,50,"Vocabulary",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))

    def handle_event(self, event): 
        for button in self.buttons:
            button.handle_event(event)

    # Define relevant UI buttons and bind actions from the gamestate
    def update(self):
        if self.gamestate.current_state == 'main':
            self.buttons = [self.main_button, self.stats_button, self.vocab_button]
        elif self.gamestate.current_state == 'stats':
            self.buttons = [self.main_button, self.stats_button, self.vocab_button]
        elif self.gamestate.current_state == 'vocab':
            # Initialize buttons for current item
            self.item_button = Button(200,200,200,50,self.gamestate.data.question,self.font,WHITE,WHITE,lambda: self.gamestate.change_state('vocab'))
            self.option1_button = Button(100,300,200,50,self.gamestate.data.answer,self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))
            self.option2_button = Button(400,300,200,50,self.gamestate.data.alternatives[0],self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))
            self.option3_button = Button(100,400,200,50,self.gamestate.data.alternatives[1],self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))
            self.option4_button = Button(400,400,200,50,self.gamestate.data.alternatives[2],self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))
            
            self.buttons = [
                self.main_button,
                self.item_button,
                self.option1_button,
                self.option2_button,
                self.option3_button,
                self.option4_button
                ]

    def render(self):
        self.screen.fill((0, 0, 0))
        
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.update() # Cast updates to the display