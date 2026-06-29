
def screen_iso(px, py):
    px -= 960
    py -= 100

    tile_x = (px / 34 + py / 19) / 2
    tile_y = (py / 19 - px / 34) / 2

    return int(tile_x), int(tile_y)


def can_move(map_data, px, py):
    px -= 960
    py -= 100

    tile_x = int((px / 34 + py / 19) / 2)
    tile_y = int((py / 19 - px / 34) / 2)

    valeur_case = map_data[tile_y][tile_x]
    print(f"Tentative vers tile ({tile_x}, {tile_y}) - Valeur dans la map : {valeur_case}")

    if 0 <= tile_y < len(map_data):
        if 0 <= tile_x < len(map_data[tile_y]):
            # Si ta map contient '0' pour le sol, vérifie bien que tu compares avec '0'
            return int(valeur_case) == 1

    return False