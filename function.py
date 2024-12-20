from main import RECT_SIZE
from classes import Tile, Tiles
import random


def generate_map(width: int, height: int):
    tile_map = []
    for y in range(0, height, RECT_SIZE):
        row = []
        for x in range(0, width, RECT_SIZE):
            # Generate clusters
            cluster_size = random.randint(1, 5)
            start_x = x
            start_y = y
            for _ in range(cluster_size):
                tile_type = random.choice(list(Tiles)) 
                tile = Tile(start_x, start_y, tile_type)
                row.append(tile)
                start_x += RECT_SIZE
                if start_x >= width:
                    start_x = x
                    start_y += RECT_SIZE
        tile_map.append(row)
    return tile_map

