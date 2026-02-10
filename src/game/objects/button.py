import pygame
from config import FONT

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color=(0, 255, 0), color2=(0, 255, 0), text="", textCoords=(), textColor=(255, 255, 255), textSize=30):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.color2 = color2
        self.text = text
        self.textCoords = textCoords
        self.textColor = textColor
        self.textSize = textSize

        self.isUnderCursor = False

        FONT.render_to(self.image, self.textCoords, self.text, self.textColor, size=self.textSize)

    def update(self, cursorPos):
        if self.rect.x <= cursorPos[0] <= self.rect.x + self.rect.width and self.rect.y <= cursorPos[1] <= self.rect.y + self.rect.height:
            self.isUnderCursor = True
            self.image.fill(self.color2)
        else:
            self.isUnderCursor = False
            self.image.fill(self.color)
        FONT.render_to(self.image, self.textCoords, self.text, self.textColor, size=self.textSize)
