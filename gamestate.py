class Gamestate:
    def __init__(self):
        self.current_state = None
    
    def get_state(self):
        if self.current_state == None:
            self.current_state = 'vocab'

    def update(self):
        pass