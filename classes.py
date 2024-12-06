from pygame import Rect
from enum import Enum

class Tiles(Enum):
    GROUND = 1
    WATER = 2
    CONCRETE = 3
    GRASS = 4

class Tile(Rect):
    def __init__(self, x: int, y: int, type:Tiles):
