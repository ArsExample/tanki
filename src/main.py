import pygame
import sys
import os

from game import *

sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Tanki")

    game = Game()

    game.run()
