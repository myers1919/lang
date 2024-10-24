import pygame
import sys

from gamestate import Gamestate
from ui import UI

from config import *


def main():
    print('*'*50)
    pygame.init()
    pygame.mixer.init()

    gamestate = Gamestate()
    ui = UI(gamestate)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ui.handle_event(event)
        gamestate.update()
        ui.update()
        ui.render()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()