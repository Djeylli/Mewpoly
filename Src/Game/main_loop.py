import pygame

from Event.event_window import handle_close_event

def main_loop(screen, clock, state):
    while state.running:
        state.running = handle_close_event()
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()