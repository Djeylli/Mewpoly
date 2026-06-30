import pygame
from Include.player import Player
from Include.button import Button
from Include.state import State
from Maps.read_map import open_map_file

def init_map():
    map_data = open_map_file("Src/Maps/map.txt")
    return map_data

def init_ground():
    image = pygame.image.load("Src/Assets/Isometric/isometric_block (12).png").convert_alpha()
    image = pygame.transform.scale(image, (68, 68))
    return image

def init_button():
    font = pygame.font.Font("Src/Assets/font.ttf", 128)

    button_roll = Button(
        text="",
        pos=(810, 390),
        size=(300, 60),
        action=State.ROLL_DICE,
        font=font,
        color=(0, 0, 0, 255),
        border_radius=12,
        alpha=200,
        hover_alpha=255
    )
    return button_roll

def init_player():

    player = Player(
        pos= (960, 150),
        size= (50,60),
        skin= ("Src/Assets/BlackCat_Free_Carysaurus/Black-Idle.png"),
        speed= 2,
        health= 100,
        strength= 50,
        attack= 15,
        defense= 20,
        name= "Mewpoly",
        level= 5,
        power= "griffe",
        money= 200,
    )


    return player

def init_game():
    return init_player(), init_button(), init_ground(), init_map()
