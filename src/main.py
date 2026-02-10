import pygame
import pygame.freetype
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    pygame.init()
    pygame.freetype.init()
    # pygame.mixer.init()
    pygame.display.set_caption("Tanki")

    from game import *

    game = Game()

    game.run()
