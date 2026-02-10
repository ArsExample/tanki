import pygame

from ..objects import button
from .play_state import Play_state

class Menu_state:
    def __init__(self, change_state_callback):
        self.change_state_callback = change_state_callback

        self.buttons = pygame.sprite.Group()

        self.buttonPlay = button.Button(600, 350, 400, 200, color2=(0, 225, 0), text="Играть хули", textCoords=(90, 80), textSize=40)
        self.buttons.add(self.buttonPlay)

    def draw(self, screen):
        screen.fill((0, 0, 0))

        self.buttons.draw(screen)

    def update(self):
        self.buttons.update(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.buttonPlay.isUnderCursor:
                    print("play")
                    self.change_state_callback(Play_state())
                    
