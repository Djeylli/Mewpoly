import pygame
from Play.can_move import can_move

class Player():

    def __init__(self, pos, size, skin, speed, health, strength, attack, defense, name, level, power, money):
        self.size = pygame.math.Vector2(size)
        self.color = color(*color)
        self.speed = speed
        self.speed = speed
        self.health = health
        self.strength = strength
        self.attack = attack
        self.defense = defense
        self.name = name
        self.level = level
        self.power = power
        self.money = money
        self.skin = pygame.image.load(skin).convert()
        self.rect = self.skin.get_rect()
        self.rect.topleft = pos
        self.frame = pygame.Rect(0, 0, self.size.x, self.size.y)
        self.skin.set_colorkey((0, 0, 0))
        self.hitbox = pygame.Rect(pos[0], pos[1], 20, 10)
        self.visual_pos = pygame.math.Vector2(pos)

    def move(self, map_data):

        keys = pygame.key.get_pressed()

        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        print(f"Inputs: dx={dx}, dy={dy}") 

        offset_x = self.size.x / 2
        offset_y = self.size.y

        if can_move(map_data, self.rect.x + dx + offset_x, self.rect.y + offset_y):
            self.rect.x += dx

        if can_move(map_data, self.rect.x + offset_x, self.rect.y + dy + offset_y):
            self.rect.y += dy
        self.visual_pos.x = self.rect.x
        self.visual_pos.y = self.rect.y



    def draw(self, screen):
        draw_x = self.visual_pos.x - (self.size.x / 2)
        draw_y = self.visual_pos.y - self.size.y
        screen.blit(self.skin, (draw_x, draw_y), self.frame)

