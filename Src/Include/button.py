import pygame
from collections import namedtuple

Color = namedtuple('Color', ['r', 'g', 'b', 'a'])

class Button():

    def __init__(self, text, pos, size, action, font, color, border_radius):
        self.text = text
        self.pos = pygame.math.Vector2(pos)
        self.size = pygame.math.Vector2(size)
        self.action = action
        self.font = font
        self.color = Color(*color)
        self.border_radius = border_radius
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        translucent_color = 100
        hover_color = 220
        is_hovered = self.rect.collidepoint(mouse_pos)
        self.color = self.color._replace(a=hover_color if is_hovered else translucent_color)
        btn_surface = pygame.Surface((self.size.x, self.size.y), pygame.SRCALPHA)
        pygame.draw.rect(btn_surface, tuple(self.color), btn_surface.get_rect(), border_radius= self.border_radius)
        screen.blit(btn_surface, (self.pos.x, self.pos.y))
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center= self.rect.center)
        text_shadow = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_shadow, (text_rect.x + 2, text_rect.y + 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]