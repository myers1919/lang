from logger import Logger

from data import Data

class Gamestate:
    def __init__(self):
        self.logger = Logger()
        self.current_state = None # Set default current state to NoneType
        self.previous_state = None # Set default previous state to NoneType
        print(f"GAMESTATE > CONSTRUCTOR: Default current state set to {self.current_state}.")
        print(f"GAMESTATE > CONSTRUCTOR: Default previous state set to {self.previous_state}.")
        self.data = Data()
        self.items_loaded = False

    def change_state(self, new_state):
        self.previous_state = self.current_state # Set previous state to the current state
        self.current_state = new_state # Set current state to the new state
        print(f"GAMESTATE > CHANGE_STATE: Previous state has been changed to {self.previous_state}.")
        print(f"GAMESTATE > CHANGE_STATE: Current state has been changed to {self.current_state}.")

    def update(self):
        if self.current_state == None: # Always change None state to Main state
            self.change_state('main')
        if self.current_state == 'main':
            self.items_loaded = False # Unload current items
        if self.current_state == 'stats':
            self.items_loaded = False # Unload current items
        if self.current_state == 'vocab':
            if self.items_loaded == False:
                self.data.get_items()
                self.items_loaded = True