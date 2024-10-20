from archive.item import ItemManager
from mode import ModeManager

class Gamestate:
    def __init__(self):
        self.current_state = None
        ###self.mode_manager = ModeManager()
        self.item_manager = ItemManager()
        self.button_actions = {
            'initiate_vocab': self.change_state('vocab')
        }
    
    def get_state(self):
        if self.current_state == None:
            self.current_state = 'main'

    def change_state(self, new_state):
        self.current_state = new_state

    def update(self):
        if self.current_state == None:
            self.current_state = 'main'