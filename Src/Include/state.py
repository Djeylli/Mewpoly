from enum import Enum, auto

class State(Enum):
    MAP = auto()
    MENU = auto()
    PLAY = auto()
    PAUSE = auto()
    SETTING = auto()
    GAME_OVER = auto()

class GameState():

    def __init__(self):
        self.running = True
        self.state = State.MENU