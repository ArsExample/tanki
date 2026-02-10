# игра
import pygame
import json

from network import client
from config import WIDTH, HEIGHT, SQUARE_SIZE
from ..objects import *

class Play_state:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.player1_group = pygame.sprite.Group()
        self.player2_group = pygame.sprite.Group()
        self.player = Player(300, 300)
        self.player2 = Player(1200, 300, color=(0, 0, 255))
        self.shadow = Player(300, 300)
        self.players.add(self.player)
        self.players.add(self.player2)
        self.player1_group.add(self.player)
        self.player2_group.add(self.player2)

        self.walls = pygame.sprite.Group()
        self.wall1 = Wall(150, 150)
        self.wall2 = Wall(200, 150)
        self.wall3 = Wall(200, 200)
        self.wall4 = Wall(100, 150)
        self.walls.add(self.wall1)
        self.walls.add(self.wall2)
        self.walls.add(self.wall3)
        self.walls.add(self.wall4)

        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()

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
            d = self.client.msg_queue.get()
            for i in d.split("|"):
                if i != "":
                    i = json.loads(i)
                    if i["class"] == "player":
                        self.player2.move = i["move"]
                    elif i["class"] == "bullet":
                        self.bullets2.add(Bullet(self.player2.rect.centerx, self.player2.rect.centery, i["move"]))

            # self.player2.rect.x = int(d[0])
            # self.player2.rect.y = int(d[1])

        self.player.update(self.walls, self.shadow)
        self.player2.update(self.walls, self.shadow)
        self.bullets1.update()
        self.bullets2.update()

        pygame.sprite.groupcollide(self.bullets1, self.walls, True, False)  
        pygame.sprite.groupcollide(self.bullets2, self.walls, True, False)  
        collided = pygame.sprite.groupcollide(self.player1_group, self.bullets2, True, True)  
        collided2 = pygame.sprite.groupcollide(self.player2_group, self.bullets1, True, True)  
        print(collided, collided2)

        # msg = str(self.player.rect.x) + "," + str(self.player.rect.y)
        # self.client.send_msg(msg)
        
    def draw(self, screen):
        screen.fill((0, 0, 0))

        self.walls.draw(screen)
        self.bullets1.draw(screen)
        self.bullets2.draw(screen)
        
        for i in range(32):
            pygame.draw.line(screen, (255, 255, 255), (SQUARE_SIZE*(i+1), 0), (SQUARE_SIZE*(i+1), HEIGHT), 1)
        for i in range(18):
            pygame.draw.line(screen, (255, 255, 255), (0, SQUARE_SIZE*(i+1)), (WIDTH, SQUARE_SIZE*(i+1)), 1)

        self.players.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.move = self.player.directions[3]
                data = {
                    "class": "player",
                    "move": "up"
                }
                self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_a:
                self.player.move = self.player.directions[1]
                data = {
                    "class": "player",
                    "move": "left"
                }
                self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_s:
                self.player.move = self.player.directions[4]
                data = {
                    "class": "player",
                    "move": "down"
                }
                self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_d:
                self.player.move = self.player.directions[2]
                data = {
                    "class": "player",
                    "move": "right"
                }
                self.client.send_msg(json.dumps(data))

            if event.key == pygame.K_r:
                self.bullets1.add(Bullet(self.player.rect.centerx, self.player.rect.centery, self.player.direction))
                data = {
                    "class": "bullet",
                    "move": self.player.direction
                }
                self.client.send_msg(json.dumps(data))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if self.player.move == self.player.directions[3]:
                    self.player.move = self.player.directions[0]
                    data = {
                        "class": "player",
                        "move": "none"
                    }
                    self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_a:
                if self.player.move == self.player.directions[1]:
                    self.player.move = self.player.directions[0]
                    data = {
                        "class": "player",
                        "move": "none"
                    }
                    self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_s:
                if self.player.move == self.player.directions[4]:
                    self.player.move = self.player.directions[0]
                    data = {
                        "class": "player",
                        "move": "none"
                    }
                    self.client.send_msg(json.dumps(data))
            elif event.key == pygame.K_d:
                if self.player.move == self.player.directions[2]:
                    self.player.move = self.player.directions[0]
                    data = {
                        "class": "player",
                        "move": "none"
                    }
                    self.client.send_msg(json.dumps(data))
