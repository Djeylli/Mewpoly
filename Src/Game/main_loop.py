import pygame

from Event.event_window import handle_close_event
from Include.dict_state import dict_state

def main_loop(screen, clock, state):
    while state.running:
        events = pygame.event.get()
        state.running = handle_close_event(events)
        screen.fill("white")
        dict_state[state.state](screen, state, events)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()