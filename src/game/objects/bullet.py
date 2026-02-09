import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, color=(255, 255, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.directions = ["left", "right", "up", "down"]
        self.move = direction
        self.velX = 0
        self.velY = 0

    def update(self):
        if self.move == self.directions[0]:
            self.velX = -10
            self.velY = 0
        elif self.move == self.directions[1]:
            self.velX = 10
            self.velY = 0
        elif self.move == self.directions[2]:
            self.velX = 0
            self.velY = -10
        elif self.move == self.directions[3]:
            self.velX = 0
            self.velY = 10

        if not self.check_col():
            self.rect.x += self.velX
            self.rect.y += self.velY

    def check_col(self):
        return False
