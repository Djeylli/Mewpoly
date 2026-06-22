import pygame
from Include.button import Button
from Include.state import State

def init_bg_menu():
    bg = pygame.image.load("Src/Assets/bg_menu.png")
    bg = bg.convert()
    info = pygame.display.Info()
    bg = pygame.transform.scale(bg, (info.current_w, info.current_h))
    return bg

def init_button():
    font = pygame.font.Font("Src/Assets/font.ttf", 64)

    buttons = [
        Button(
            text="Jouer",
            pos=(810, 390),
            size=(300, 60),
            action=State.MAP,
            font=font,
            color=(255, 255, 255, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=0
        ),
        Button(
            text="Options",
            pos=(810, 490),
            size=(300, 60),
            action=None,
            font=font,
            color=(255, 255, 255, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=0
        ),
        Button(
            text="Quitter",
            pos=(810, 690),
            size=(300, 60),
            action=None,
            font=font,
            color=(255, 255, 255, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=0
        ),
    ]
    return buttons

def init_menu():
    return init_button(), init_bg_menu()