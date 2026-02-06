import pygame

from game import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My Game")

game = Game()

game.run()
