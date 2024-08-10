import pygame
import sys

from gamestate import Gamestate
from ui import UI

def main():
    pygame.init()
    pygame.mixer.init()

    ui = UI()
    gamestate = Gamestate()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pass

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()