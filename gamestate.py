from logger import Logger

from data import Data

class Gamestate:
    def __init__(self):
        self.logger = Logger()
        self.current_state = None # Set default current state to NoneType
        self.previous_state = None # Set default previous state to NoneType
        self.data = Data()
        print(f"GAMESTATE > CONSTRUCTOR: Default current state set to {self.current_state}.")
        print(f"GAMESTATE > CONSTRUCTOR: Default previous state set to {self.previous_state}.")

    def change_state(self, new_state):
        self.previous_state = self.current_state # Set previous state to the current state
        self.current_state = new_state # Set current state to the new state
        print(f"GAMESTATE > CHANGE_STATE: Previous state has been changed to {self.previous_state}.")
        print(f"GAMESTATE > CHANGE_STATE: Current state has been changed to {self.current_state}.")

    def update(self):
        # Always change None state to Main state
        if self.current_state == None:
            self.change_state('main')
        if self.current_state == 'main':
            pass
        if self.current_state == 'vocab':
            pass