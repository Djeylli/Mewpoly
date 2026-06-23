

def open_map_file(map_name):
    fd = open(map_name)
    map = [[int(c) for c in row] for row in fd.read().split('\n')]
    fd.close()
    return map