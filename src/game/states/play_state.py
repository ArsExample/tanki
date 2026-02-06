# игра
import pygame
from config import WIDTH, HEIGHT
from ..objects import *

class Play_state:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.player = Player(300, 300)
        self.player2 = Player(1200, 300, color=(0, 0, 255))
        self.shadow = Player(300, 300)
        self.players.add(self.player)
        self.players.add(self.player2)

        self.walls = pygame.sprite.Group()
        self.wall1 = Wall(150, 150)
        self.wall2 = Wall(200, 150)
        self.wall3 = Wall(200, 200)
        self.wall4 = Wall(100, 150)
        self.walls.add(self.wall1)
        self.walls.add(self.wall2)
        self.walls.add(self.wall3)
        self.walls.add(self.wall4)

    def update(self):
        self.player.update(self.walls, self.shadow)

        # msg = str(player.rect.x) + "," + str(player.rect.y)
        # client.send(msg.encode())
        

    def draw(self, screen):
        screen.fill((0, 0, 0))

        self.walls.draw(screen)
        
        for i in range(32):
            pygame.draw.line(screen, (255, 255, 255), (50*(i+1), 0), (50*(i+1), HEIGHT), 1)
        for i in range(18):
            pygame.draw.line(screen, (255, 255, 255), (0, 50*(i+1)), (WIDTH, 50*(i+1)), 1)

        self.players.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.move = self.player.directions[3]
            elif event.key == pygame.K_a:
                self.player.move = self.player.directions[1]
            elif event.key == pygame.K_s:
                self.player.move = self.player.directions[4]
            elif event.key == pygame.K_d:
                self.player.move = self.player.directions[2]
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if self.player.move == self.player.directions[3]:
                    self.player.move = self.player.directions[0]
            elif event.key == pygame.K_a:
                if self.player.move == self.player.directions[1]:
                    self.player.move = self.player.directions[0]
            elif event.key == pygame.K_s:
                if self.player.move == self.player.directions[4]:
                    self.player.move = self.player.directions[0]
            elif event.key == pygame.K_d:
                if self.player.move == self.player.directions[2]:
                    self.player.move = self.player.directions[0]
