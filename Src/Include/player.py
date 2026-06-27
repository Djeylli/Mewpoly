import pygame

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


    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.skin, self.rect, self.frame)

