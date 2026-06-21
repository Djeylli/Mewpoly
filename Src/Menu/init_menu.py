import pygame
from Include.button import Button
from Include.state import State

def init_bg_menu():
    bg = pygame.image.load("Src/Assets/bg_menu.png")
    bg = bg.convert()
    bg = pygame.transform.scale(bg, (1920, 1080))
    return bg

def init_button():
    font = pygame.font.Font("Src/Assets/font.ttf", 32)

    buttons = [
        Button(
            text="Jouer",
            pos=(810, 390),
            size=(300, 60),
            action=State.PLAY,
            font=font,
            color=(15, 45, 60, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=220
        ),
        Button(
            text="Options",
            pos=(810, 470),
            size=(300, 60),
            action=State.SETTING,
            font=font,
            color=(15, 45, 60, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=220
        ),
        Button(
            text="Quitter",
            pos=(810, 630),
            size=(300, 60),
            action=None,
            font=font,
            color=(15, 45, 60, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=220
        ),
    ]
    return buttons


def init_menu():
    return init_button(), init_bg_menu()