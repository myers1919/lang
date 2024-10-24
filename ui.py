import pygame
import random

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
        self.main_button = Button(10,540,200,50,"Main Menu",self.font,PINK,PINK_HOVER,lambda: self.gamestate.change_state('main'))
        self.stats_button = Button(150,200,200,50,"Statistics",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('stats'))
        self.vocab_button = Button(450,200,200,50,"Vocabulary",self.font,YELLOW,YELLOW_HOVER,lambda: self.gamestate.change_state('vocab'))

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
            if self.gamestate.awaiting_response == False:
                self.item_button = Button(300,200,200,50,self.gamestate.data.question,self.font,YELLOW,YELLOW,lambda: self.gamestate.change_state('vocab'))
                option_button_locations = [[150,300],[450,300],[150,375],[450,375]]
                print(f"Before shuffle: {option_button_locations}")
                random.shuffle(option_button_locations)
                print(f"After shuffle: {option_button_locations}")
                self.option1_button = Button(option_button_locations[0][0],option_button_locations[0][1],200,50,self.gamestate.data.answer,self.font,WHITE,WHITE_HOVER,lambda: self.gamestate.get_result(True))
                self.option2_button = Button(option_button_locations[1][0],option_button_locations[1][1],200,50,self.gamestate.data.alternatives[0],self.font,WHITE,WHITE_HOVER,lambda: self.gamestate.get_result(False))
                self.option3_button = Button(option_button_locations[2][0],option_button_locations[2][1],200,50,self.gamestate.data.alternatives[1],self.font,WHITE,WHITE_HOVER,lambda: self.gamestate.get_result(False))
                self.option4_button = Button(option_button_locations[3][0],option_button_locations[3][1],200,50,self.gamestate.data.alternatives[2],self.font,WHITE,WHITE_HOVER,lambda: self.gamestate.get_result(False))

                self.buttons = [
                    self.main_button,
                    self.item_button,
                    self.option1_button,
                    self.option2_button,
                    self.option3_button,
                    self.option4_button
                    ]

                self.gamestate.awaiting_response = True

    def render(self):
        self.screen.fill((0, 0, 0))
        
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.update() # Cast updates to the display