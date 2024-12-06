from pygame import Rect, image, transform, K_RIGHT, K_LEFT, K_UP, K_DOWN, font, draw
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CIRCLE_RADIUS
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

class Player(Sprite):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 50
        self.rect = Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, CIRCLE_RADIUS, CIRCLE_RADIUS)

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
        self.image = image.load(image_path)#.convert()
        self.image = transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface, cx: int, cy: int):
        surface.blit(self.image, self.rect.move(-cx, -cy))



class PlayerDraw(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, 'entities/drone.png')
        self.name = name
        self.font = font.SysFont('Arial', 30)

    def draw_text(self, surface, cx, cy):
        self.text_surface = self.font.render(self.name, True, (255, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx = self.rect.centerx  # Center the text horizontally
        self.text_rect.bottom = self.rect.top - 10
        surface.blit(self.text_surface, self.text_rect.move(-cx, -cy))

    def draw(self, surface, cx, cy):
         surface.blit(self.image, self.rect.move(-cx, -cy))
         self.draw_text(surface, cx, cy)

class ActiveProvider(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'entities/active_provider.png')
        self.font = font.SysFont('Arial', 30)
        self.text_surfaces = []  # List to hold surfaces for each line of text
        self.text_rects = []     # List to hold rects for each line of text
        self.count = 0

    def update_text_position(self):
        """Update the position of the text based on the object's position."""
        for i, text_rect in enumerate(self.text_rects):
            text_rect.centerx = self.rect.centerx  # Center each line horizontally
            text_rect.bottom = self.rect.top - 10 - (i * (self.font.get_height() + 2))  # Position it above the object

    def create_request(self, text: str):
        """Create a request with multi-line text."""
        self.count +=1
        lines = text.split('\n')  # Split the text into lines
        self.text_surfaces = [self.font.render(line, True, (0, 0, 0)) for line in lines]  # Render each line
        self.text_rects = [surface.get_rect() for surface in self.text_surfaces]  # Get rects for each line

    def draw(self, surface, cx: int, cy: int):
        """Draw the object and the text on the screen."""
        surface.blit(self.image, self.rect.move(-cx, -cy))  # Draw the object
        self.update_text_position()  # Update the text position
        for text_surface, text_rect in zip(self.text_surfaces, self.text_rects):
            surface.blit(text_surface, text_rect.move(-cx, -cy))  # Draw each line of text


class Requester(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'entities/active_provider.png')
        self.font = font.SysFont('Arial', 30)
        self.text_surfaces = []  # List to hold surfaces for each line of text
        self.text_rects = []     # List to hold rects for each line of text
        self.count = 0

    def update_text_position(self):
        """Update the position of the text based on the object's position."""
        for i, text_rect in enumerate(self.text_rects):
            text_rect.centerx = self.rect.centerx  # Center each line horizontally
            text_rect.bottom = self.rect.top - 10 - (i * (self.font.get_height() + 2))  # Position it above the object

    def create_request(self, text: str):
        """Create a request with multi-line text."""
        self.count +=1
        lines = text.split('\n')  # Split the text into lines
        self.text_surfaces = [self.font.render(line, True, (0, 0, 0)) for line in lines]  # Render each line
        self.text_rects = [surface.get_rect() for surface in self.text_surfaces]  # Get rects for each line

    def draw(self, surface, cx: int, cy: int):
        """Draw the object and the text on the screen."""
        surface.blit(self.image, self.rect.move(-cx, -cy))  # Draw the object
        self.update_text_position()  # Update the text position
        for text_surface, text_rect in zip(self.text_surfaces, self.text_rects):
            surface.blit(text_surface, text_rect.move(-cx, -cy))  # Draw each line of text


class TestEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'entities/test.png')




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
