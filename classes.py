from typing import Self
from pygame import Rect, image, transform
from enum import Enum


class Tiles(Enum):
    GROUND = 1
    WATER = 2
    CONCRETE = 3
    GRASS = 4

class Tile(Rect):
    def __init__(self, x: int, y: int, tile_type: Tiles):
        super().__init__(x, y, 10, 10)
        self.x = x
        self.y = y
        self.tile_type = type
        self.image = image.load(get_tile_path(tile_type))
        self.image = transform.scale(self.image, (100, 100))  # Scale to 100x100 pixels
        self.rect = self.image.get_rect(topleft=(x, y))  # Get the rectangle for positioning

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class World:
    def __init__(self):
        """Initialize the world with a grid of tiles."""
        self.tiles = [Tile(10, 10, Tiles.CONCRETE)]

    # def draw(self, surface):
    #     """Draw all tiles in the world on the given surface."""
    #     for row in self.tiles:
    #         for tile in row:
    #             tile.draw(surface)
    #
    #
def get_tile_path(t: Tiles):
    return {Tiles.WATER:'map_tiles/water.png',
            Tiles.GROUND:'map_tiles/ground.png',
            Tiles.CONCRETE:'map_tiles/concrete.png',
            Tiles.GRASS:'map_tiles/grass.png',
        }[t]


