from enum import Enum, auto
from Menu.play_menu import play_menu
from Maps.play_map import play_map
from Play.play_game import play_game
from Pause.play_pause import play_pause
from Settings.play_settings import play_settings
from GameOver.play_game_over import play_game_over

class State(Enum):
    MAP = auto()
    MENU = auto()
    PLAY = auto()
    PAUSE = auto()
    SETTING = auto()
    GAME_OVER = auto()

dict_state = {
    State.MAP: play_map,
    State.MENU: play_menu,
    State.PLAY: play_game,
    State.PAUSE: play_pause,
    State.SETTING: play_settings,
    State.GAME_OVER: play_game_over
}

class GameState():

    def __init__(self):
        self.running = True
        self.state = State.MENU