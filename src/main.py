import pygame

from game import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Tanki")

game = Game()

game.run()
