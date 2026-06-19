from enum import Enum, auto

class state(Enum):
    MAP = auto()
    MENU = auto()
    PLAY = auto()
    START = auto()
    PAUSE = auto()
    SETTING = auto()
    GAME_OVER = auto()

class GameState():

    def __init__(self):
        self.running = True
        self.state = state.MENU