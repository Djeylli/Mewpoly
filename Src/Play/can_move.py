
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

    if 0 <= tile_y < len(map_data) and 0 <= tile_x < len(map_data[tile_y]):
        return int(map_data[tile_y][tile_x]) == 1

    return False