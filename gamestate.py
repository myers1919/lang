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
        self.awaiting_response = False

    def change_state(self, new_state):
        self.previous_state = self.current_state # Set previous state to the current state
        self.current_state = new_state # Set current state to the new state
        print(f"GAMESTATE > CHANGE_STATE: Previous state has been changed to {self.previous_state}.")
        print(f"GAMESTATE > CHANGE_STATE: Current state has been changed to {self.current_state}.")
        self.reset_item_flags()
        print(f"Item flags have been reset.")

    def update(self):
        if self.current_state == None: # Always change None state to Main state
            self.change_state('main')
        if self.current_state == 'main':
            pass
            ###self.reset_item_flags() # Unload current items
        if self.current_state == 'stats':
            #self.reset_item_flags() # Unload current items
            pass
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
            if len(self.data.item_set) == 0:
                self.change_state('main')
                print("Vocab exercise complete. Kicking back to main.")
                #self.data.item_set = None
        
    def reset_item_flags(self):
        '''
        Resets all item-related flags to False so that a new item may be prepared.
        '''
        self.items_loaded = False
        self.current_item_is_selected = False
        self.current_alternatives_is_selected = False
        self.awaiting_response = False

    def get_result(self,result):
        '''
        Checks answer. Resets flag so the next question can be loaded.
        '''
        self.data.item_set = self.data.item_set[1:]
        self.current_item_is_selected = False
        self.awaiting_response = False
        if result == True:
            print("That's correct!")
            print(f"Updating item with ID: {self.data.id}")
            # Increment number of times the item has been seen
            self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_seen'] += 1
            self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_correct'] += 1
            ###df.loc[df['id'] == 14, 'count'] += 1
        if result == False:
            print("That is incorrect.")
            print(f"Updating item with ID: {self.data.id}")
            # Increment number of times the item has been seen
            self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_seen'] += 1
            self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_incorrect'] += 1
        n_seen = self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_seen']
        n_correct = self.data.stats.loc[self.data.stats['id'] == self.data.id, 'n_correct']
        self.data.stats.loc[self.data.stats['id'] == self.data.id, '%_correct'] = n_correct / n_seen # Update % correct
        self.data.stats = self.data.stats.sort_values(by=['n_seen','%_correct'], ascending=[False,False])
        print(f"There are {len(self.data.item_set)} items remaining in the set.")
        self.current_alternatives_is_selected = False # Dump alternatives so new ones may be selected
        self.data.stats.to_csv('data/stats.csv', index=False, encoding="utf-8") # Update saved version of stats .csv