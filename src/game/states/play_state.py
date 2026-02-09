# игра
import pygame
import json

from network import client
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

        self.bullets = pygame.sprite.Group()

        # network
        self.client = client.Client()
        self.client.connect()
        data = json.loads(self.client.recieve_msg())
        self.player.rect.x = int(data["x1"])
        self.player.rect.y = int(data["y1"])
        self.player2.rect.x = int(data["x2"])
        self.player2.rect.y = int(data["y2"])
        self.client.start_recieve()

    def update(self):
        while not self.client.msg_queue.empty():
            d = self.client.msg_queue.get().split(",")
            self.player2.rect.x = int(d[0])
            self.player2.rect.y = int(d[1])

        self.player.update(self.walls, self.shadow)
        self.bullets.update()

        pygame.sprite.groupcollide(self.bullets, self.walls, True, False)  # тут типа col = groupcollide и внутри должны быть спрайты

        msg = str(self.player.rect.x) + "," + str(self.player.rect.y)
        self.client.send_msg(msg)
        
    def draw(self, screen):
        screen.fill((0, 0, 0))

        self.walls.draw(screen)
        self.bullets.draw(screen)
        
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

            if event.key == pygame.K_SPACE:
                self.bullets.add(Bullet(self.player.rect.centerx, self.player.rect.centery, self.player.direction))
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
