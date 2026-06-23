import pygame
from Maps.init_map import init_map

buttons, bg_maps = None, None

def play_map(screen, state):
    global buttons, bg_maps

    if buttons is None:
        buttons, bg_maps = init_map()
    screen.blit(bg_maps, (0, 0))
    for btn in buttons:
        btn.draw(screen)
        if btn.is_clicked():
            state.state = btn.action
