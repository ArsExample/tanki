import pygame
from config import SQUARE_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(0, 255, 0), second_player=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.directions = ["none", "left", "right", "up", "down"]
        self.move = self.directions[0]
        self.direction = "up"
        self.velX = 0
        self.velY = 0
        self.second_player = second_player
        
        
    def update(self, walls, shadow):
        if self.move == self.directions[0]:
            self.velX = 0
            self.velY = 0
        elif self.move == self.directions[1]:
            self.velX = -5
            self.velY = 0
            self.direction = self.directions[1]
        elif self.move == self.directions[2]:
            self.velX = 5
            self.velY = 0
            self.direction = self.directions[2]
        elif self.move == self.directions[3]:
            self.velX = 0
            self.velY = -5
            self.direction = self.directions[3]
        elif self.move == self.directions[4]:
            self.velX = 0
            self.velY = 5
            self.direction = self.directions[4]

        if not self.second_player:
            if not self.check_col(walls, shadow):
                self.rect.x += self.velX
                self.rect.y += self.velY
        else:
            self.rect.x += self.velX
            self.rect.y += self.velY



    def check_col(self, walls, shadow):  # true if collision
        shadow.rect.x = self.rect.x + self.velX
        shadow.rect.y = self.rect.y + self.velY
        if pygame.sprite.spritecollide(shadow, walls, False):
            return True
        return False
