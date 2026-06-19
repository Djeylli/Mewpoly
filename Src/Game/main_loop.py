import pygame

from Event.event_window import handle_close_event
from Include.state import State, dict_state

def main_loop(screen, clock, state):
    while state.running:
        state.running = handle_close_event()
        screen.fill("black")
        dict_state[state.state](screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()