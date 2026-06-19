import pygame

def handle_close_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True