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
        self.current_item_is_selected = False
        self.current_alternatives_is_selected = False

    def change_state(self, new_state):
        self.previous_state = self.current_state # Set previous state to the current state
        self.current_state = new_state # Set current state to the new state
        print(f"GAMESTATE > CHANGE_STATE: Previous state has been changed to {self.previous_state}.")
        print(f"GAMESTATE > CHANGE_STATE: Current state has been changed to {self.current_state}.")

    def update(self):
        if self.current_state == None: # Always change None state to Main state
            self.change_state('main')
        if self.current_state == 'main':
            self.reset_item_flags() # Unload current items
        if self.current_state == 'stats':
            self.reset_item_flags() # Unload current items
        ######################
        ### Vocabulary Mode
        ######################
        if self.current_state == 'vocab':
            if self.items_loaded == False:
                self.data.get_items()
                self.items_loaded = True
            if self.current_item_is_selected == False: # Load a new current item if one is not already selected
                self.data.get_current_item() # Get a single item entry from the item set list
                self.data.parse_current_item() # Parse the item entry to separate the question and the answer
                self.current_item_is_selected = True
            if self.current_alternatives_is_selected == False: # Get alternative answers for current item
                self.data.get_current_alternatives()
                self.current_alternatives_is_selected = True
        
    def reset_item_flags(self):
        '''
        Resets all item-related flags to False so that a new item may be prepared.
        '''
        self.current_item_is_selected = False
        self.current_item_is_selected = False
        self.current_alternatives_is_selected = False
