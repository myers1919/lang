class Controller:
    def __init__(self, gamestate, ui):
        self.gamestate = gamestate
        self.ui = ui

    def handle_event(self, event):
        self.ui.handle_event(event)

    def update(self):
        self.gamestate.update()
        self.ui.update(self.gamestate)

    def render(self):
        pass