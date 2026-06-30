from Include.state import State
from Menu.play_menu import play_menu
from Maps.play_map import play_map
from Play.play_game import play_game
from Pause.play_pause import play_pause
from Settings.play_settings import play_settings
from GameOver.play_game_over import play_game_over

dict_state = {
    State.MAP: play_map,
    State.MENU: play_menu,
    State.PLAY: play_game,
    State.PAUSE: play_pause,
    State.SETTING: play_settings,
    State.GAME_OVER: play_game_over,
}