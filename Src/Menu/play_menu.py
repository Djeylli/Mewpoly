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
            color=(129, 236, 174, 255),
            border_radius=12
        ),
        Button(
            text="Options",
            pos=(490, 330),
            size=(300, 60),
            action=None,
            font=font,
            color=(116, 185, 255, 255),
            border_radius=12
        ),
        Button(
            text="Crédits",
            pos=(490, 410),
            size=(300, 60),
            action=None,
            font=font,
            color=(162, 155, 254, 255),
            border_radius=12
        ),
        Button(
            text="Quitter",
            pos=(490, 490),
            size=(300, 60),
            action=None,
            font=font,
            color=(255, 118, 117, 255),
            border_radius=12
        ),
    ]
    background_color = (222, 203, 164)
    screen.fill(background_color)
    for btn in buttons:
        btn.draw(screen)
    font = pygame.font.SysFont("Belleza", 80)
    title = font.render("MEWPOLY", True, (180, 140, 90))
    screen.blit(title, (490, 80))
