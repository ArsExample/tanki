# основной класс с игровым циклом
import pygame
from config import WIDTH, HEIGHT, FPS

from .states import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_state = Play_state()

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                    self.current_state.handle_event(event)

            self.current_state.update()
            self.current_state.draw(self.screen)

            pygame.display.flip()
