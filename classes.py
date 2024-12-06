from typing import Self
from pygame import Rect, image, transform, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.sprite import Sprite
from math import sqrt
from enum import Enum


class Tiles(Enum):
    WATER = 1
    NAVIS_GRASS = 2
    NAVIS_CONCRETE = 3
    NAVIS_HAZARD_CONCRETE = 4
    NAVIS_SAND = 5
    VULCANUS_LAVA = 6
    VULCANUS_VOLCANIC_SOIL = 7
    VULCANUS_VOLCANIC = 8
    FULGORA_MACHINE = 9
    FULGORA_SOIL = 10
    GLEBA_MOLD = 11
    GLEBA_MOLD2 = 12
    GLEBA_MOLD3 = 13
    AKILO_DUST = 14
    AKILO_DUST2 = 15
    AKILO_ICE = 16

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
        ...


class Entity(Sprite):
    def __init__(self, x: int, y: int, image_path: str, x_size: int = 64, y_size: int = 64):
        super().__init__()
        self.image = image.load("entities/test.png").convert()
        self.image = transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface, cx: int, cy: int):
        surface.blit(self.image, self.rect.move(-cx, -cy))

class TestEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, '123')




def get_tile_path(t: Tiles):
    return {
        Tiles.WATER:'map_tiles/water.png',
        Tiles.NAVIS_GRASS:'map_tiles/navis_grass.png',
        Tiles.NAVIS_CONCRETE:'map_tiles/navis_concrete.png',
        Tiles.NAVIS_HAZARD_CONCRETE:'map_tiles/navis_hazard_concrete.png',
        Tiles.NAVIS_SAND:'map_tiles/navis_sand.png',
        Tiles.VULCANUS_LAVA:'map_tiles/vulcanus_lava.png',
        Tiles.VULCANUS_VOLCANIC_SOIL:'map_tiles/vulcanus_volcanic_soil.png',
        Tiles.VULCANUS_VOLCANIC:'map_tiles/vulcanus_volcanic.png',
        Tiles.FULGORA_MACHINE:'map_tiles/fulgora_machine.png',
        Tiles.FULGORA_SOIL:'map_tiles/fulgora_soil.png',
        Tiles.GLEBA_MOLD:'map_tiles/gleba_mold.png',
        Tiles.GLEBA_MOLD2:'map_tiles/gleba_mold2.png',
        Tiles.GLEBA_MOLD3:'map_tiles/gleba_mold3.png',
        Tiles.AKILO_DUST:'map_tiles/akilo_dust.png',
        Tiles.AKILO_DUST2:'map_tiles/akilo_dust2.png',
        Tiles.AKILO_ICE:'map_tiles/akilo_ice.png',
    }[t]


