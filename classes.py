from typing import Self
from pygame import Rect, image, transform, K_RIGHT, K_LEFT, K_UP, K_DOWN
from math import sqrt
from enum import Enum


class Tiles(Enum):
    WATER = 2
    CONCRETE = 3
    GRASS = 4
    HAZARD_CONCRETE = 5

class Tile(Rect):
    def __init__(self, x: int, y: int, tile_type: Tiles):
        super().__init__(x, y, 128, 128)
        self.x = x
        self.y = y
        self.tile_type = type
        self.image = image.load(get_tile_path(tile_type)).convert()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 50

    def move(self, keys):
        # Movement vector
        move_x = keys[K_RIGHT] - keys[K_LEFT]
        move_y = keys[K_DOWN] - keys[K_UP]

        # Calculate the length of the movement vector
        length = sqrt(move_x**2 + move_y**2)

        # Normalize the vector if it's not zero
        if length != 0:
            move_x /= length
            move_y /= length

        # Update position based on speed
        self.x += move_x * self.speed
        self.y += move_y * self.speed
        self.x, self.y = round(self.x, 2), round(self.y, 2)


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

class Entity(Rect):
    def __init__(self, x: int, y: int, image_path: str, x_size: int = 64, y_size: int = 64):
        super().__init__(x, y, x_size, y_size)
        self.image = image.load("entities/test.png").convert()
        self.image = transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class TestEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, '123', 10, 10)

def get_tile_path(t: Tiles):
    return {Tiles.WATER:'map_tiles/water.png',
            Tiles.HAZARD_CONCRETE:'map_tiles/hazard_concrete.png',
            Tiles.CONCRETE:'map_tiles/concrete.png',
            Tiles.GRASS:'map_tiles/grass.png',
        }[t]
