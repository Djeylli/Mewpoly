from init_windows import init_windows
from main_loop import main_loop

def main():
    screen, clock, running = init_windows()
    main_loop(screen, clock, running)

if __name__ == '__main__':
    main()