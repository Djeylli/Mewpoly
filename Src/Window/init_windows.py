import pygame

def init_windows():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    pygame.display.set_caption("MewPoly")
    clock = pygame.time.Clock()
    return screen, clock