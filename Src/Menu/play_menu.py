import pygame
from Include.button import Button

def play_menu(screen):
    font = pygame.font.SysFont("Arial", 32)

    buttons = [
        Button(
            text="Jouer",
            pos=(490, 250),
            size=(300, 60),
            action=None,
            font=font,
            color=(70, 130, 180, 255),
            border_radius=12
        ),
        Button(
            text="Options",
            pos=(490, 330),
            size=(300, 60),
            action=None,
            font=font,
            color=(70, 130, 180, 255),
            border_radius=12
        ),
        Button(
            text="Crédits",
            pos=(490, 410),
            size=(300, 60),
            action=None,
            font=font,
            color=(70, 130, 180, 255),
            border_radius=12
        ),
        Button(
            text="Quitter",
            pos=(490, 490),
            size=(300, 60),
            action=None,
            font=font,
            color=(180, 70, 70, 255),
            border_radius=12
        ),
    ]
    for btn in buttons:
        btn.draw(screen)