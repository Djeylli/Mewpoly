import pygame
from Include.player import Player

def init_player():

    player = Player(

        pos= (0,0),
        size= (64,64),
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

