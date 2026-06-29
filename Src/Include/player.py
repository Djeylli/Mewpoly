import pygame

class Player():

    def __init__(self, pos, size, color, speed):
        self.pos = pygame.math.Vector2(pos)
        self.size = pygame.math.Vector2(size)
        self.color = color(*color)
        self.speed = speed


    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed




