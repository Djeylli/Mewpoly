import pygame
from Maps.read_map import open_map_file

map_data = None
image = None

def play_game(screen, state):
    global map_data, image
    if map_data is None:
        map_data = open_map_file("Src/Maps/map.txt")
        image = pygame.image.load("Src/Assets/Isometric/isometric_block (12).png").convert_alpha()
        image = pygame.transform.scale(image, (68, 68))

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                screen.blit(image, (960 + x * 34 - y * 34, 100 + x * 19 + y * 19))
