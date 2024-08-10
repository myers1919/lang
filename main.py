import pygame
import sys

from gamestate import Gamestate
from ui import UI
from controller import Controller

def main():
    pygame.init()
    pygame.mixer.init()

    ui = UI()
    gamestate = Gamestate()
    controller = Controller(gamestate, ui)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            controller.handle_event(event)
        controller.update()
        controller.render()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()