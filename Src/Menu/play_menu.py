import pygame
from Include.button import Button
from Menu.init_menu import init_menu

def play_menu(screen, flag):
    if flag == False:
        buttons, bg_menu = init_menu()
        flag = True
    screen.blit(bg_menu, (0, 0))
    for btn in buttons:
        btn.draw(screen)
