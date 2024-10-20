import pygame

from archive.button import MenuButton, VocabButton

from archive.config import *

class UI:
    def __init__ (self):
        self.screen = pygame.display.set_mode((800,600))
        self.init_buttons()

    def init_buttons(self):
        font = pygame.font.Font(None, 16)
        self.menu_button = MenuButton(200,200,200,50,"Menu",font,YELLOW,BLACK,None)
        self.vocab_button = VocabButton(500,200,200,50,"Vocab",font,YELLOW,WHITE,self.get_action('initiate_vocab'))
        
    def handle_event(self, event):
            if self.menu_button:
                self.menu_button.handle_event(event)
            if self.vocab_button:
                 self.vocab_button.handle_event(event)

    def update(self, gamestate):
        if gamestate.current_state == 'menu':
            font = pygame.font.Font(None, 16)
            self.menu_button = MenuButton(200,200,200,50,"Menu",font,WHITE,BLACK,None)
            self.vocab_button = VocabButton(500,200,200,50,"Vocab",font,WHITE,BLACK,None)

    def render(self, gamestate):
        self.menu_button.draw(self.screen)
        self.vocab_button.draw(self.screen)

    def get_action(self, action_string):
         print("HERE WE ARE.")