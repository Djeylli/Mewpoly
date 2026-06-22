import pygame
from Include.button import Button
from Include.state import State
from Maps.read_map import open_map_file
from PIL import Image, ImageFilter

def blur_surface(surface, radius=5):
    raw = pygame.image.tostring(surface, "RGB")
    img = Image.frombytes("RGB", surface.get_size(), raw)
    img = img.filter(ImageFilter.GaussianBlur(radius=radius))
    raw_blurred = img.tobytes()
    return pygame.image.fromstring(raw_blurred, surface.get_size(), "RGB")

def init_bg_map():
    info = pygame.display.Info()
    bg = pygame.image.load("Src/Assets/bg_maps.png")
    bg = bg.convert()
    bg = pygame.transform.scale(bg, (info.current_w, info.current_h))
    bg = blur_surface(bg, 15)
    return bg

def init_btn_map():
    font = pygame.font.Font("Src/Assets/font.ttf", 128)

    buttons = [
        Button(
            text=">",
            pos=(1772, 490),
            size=(128, 60),
            action=State.PLAY,
            font=font,
            color=(255, 255, 255, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=0
        ),
        Button(
            text="<",
            pos=(40, 490),
            size=(128, 60),
            action=None,
            font=font,
            color=(255, 255, 255, 255),
            border_radius=12,
            alpha=0,
            hover_alpha=0
        )
    ]
    return buttons

def init_map():
    return init_btn_map(), init_bg_map()
