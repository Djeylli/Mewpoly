import pygame

def main_loop(screen, clock, running):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("purple")
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()