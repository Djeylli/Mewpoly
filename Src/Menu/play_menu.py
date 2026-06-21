from Menu.init_menu import init_menu

buttons, bg_menu = None, None

def play_menu(screen, state):
    global buttons, bg_menu
    if buttons is None:
        buttons, bg_menu = init_menu()
    screen.blit(bg_menu, (0, 0))
    for btn in buttons:
        btn.draw(screen)
        if btn.is_clicked():
            state.state = btn.action
