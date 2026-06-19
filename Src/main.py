from Window.init_windows import init_windows
from Game.main_loop import main_loop
from Include.state import GameState

def main():
    state = GameState()
    screen, clock = init_windows()

    main_loop(screen, clock, state)

if __name__ == '__main__':
    main()