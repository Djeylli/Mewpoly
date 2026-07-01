import pygame
from Maps.read_map import open_map_file
from Play.init_game import init_game
from Play.roll_dice import roll_dice
from Include.state import State

map_data, image, player, button_roll = None, None, None, None

def draw_game(screen):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                screen.blit(image, (960 + x * 34 - y * 34 - 34, 100 + x * 19 + y * 19 - 19))
    player.move(map_data)
    player.draw(screen)
    button_roll.draw(screen)
    font = pygame.font.SysFont("Arial", 24)
    money_text = "Argent : " + str(player.money) + " €"
    text_surface = font.render(money_text, True, (0, 0, 0))
    screen.blit(text_surface, (20, 20))

def play_game(screen, state):
    global map_data, image, player, button_roll

    if map_data is None:
        player, button_roll, image, map_data = init_game()

    draw_game(screen)
    for i in range(4):
        if button_roll.is_clicked():
            print(roll_dice())
        print("****")
