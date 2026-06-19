import pygame

def init_windows():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("MewPoly")
    clock = pygame.time.Clock()
    return screen, clock