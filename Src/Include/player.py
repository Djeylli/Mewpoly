import pygame
from Play.can_move import can_move

class Player():

    def __init__(self, pos, size, skin, speed, health, strength, attack, defense, name, level, power, money):
        self.size = pygame.math.Vector2(size)
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
        self.selected = False

    def move(self, map_data):

        mouse_pos = pygame.mouse.get_pos()
        self.rect.collidepoint(mouse_pos)
        keys = pygame.key.get_pressed()
        pygame.mouse.get_pressed()

        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        if can_move(map_data, self.rect.x + dx, self.rect.y):
            self.rect.x += dx

        if can_move(map_data, self.rect.x, self.rect.y + dy):
            self.rect.y += dy
        self.visual_pos.x = self.rect.x
        self.visual_pos.y = self.rect.y

    def draw(self, screen):
        draw_x = self.visual_pos.x - (self.size.x / 2)
        draw_y = self.visual_pos.y - self.size.y
        screen.blit(self.skin, (draw_x, draw_y), self.frame)

