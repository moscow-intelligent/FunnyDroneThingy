from classes import Tile, Tiles
import random

RECT_SIZE = 128

# Определение биомов с использованием существующих тайлов
BIOMES = {
    'navis': [Tiles.NAVIS_GRASS, Tiles.NAVIS_CONCRETE, Tiles.NAVIS_HAZARD_CONCRETE, Tiles.WATER, Tiles.NAVIS_SAND],
    'vulcanus': [Tiles.VULCANUS_LAVA, Tiles.VULCANUS_VOLCANIC_SOIL, Tiles.VULCANUS_VOLCANIC],
    'fulgora': [Tiles.FULGORA_MACHINE, Tiles.FULGORA_SOIL],
    'gleba': [Tiles.GLEBA_MOLD,Tiles.GLEBA_MOLD2,Tiles.GLEBA_MOLD3, Tiles.WATER],
    'akilo': [Tiles.AKILO_DUST, Tiles.AKILO_DUST2, Tiles.AKILO_ICE, Tiles.WATER]
}

def generate_biome(x, y, biome_type):
    """Генерирует тайлы для указанного биома."""
    tiles = []
    # Генерируем тайлы для указанного биома
    for _ in range(10):  # Генерируем 5 тайлов для каждого биома
        tile_type = random.choice(BIOMES[biome_type])
        tile = Tile(x, y, tile_type)
        tiles.append(tile)
        x += RECT_SIZE
    return tiles

def generate_map(size: int):
    tile_map = []
    for y in range(0, size, RECT_SIZE):
        for x in range(0, size, RECT_SIZE):
            # Случайно выбираем биом
            biome_type = random.choices(
                list(BIOMES.keys()),
                weights=[0.4, 0.2, 0.15, 0.15, 0.1],
                k=1
            )[0]  # Используем веса для более реалистичного распределения биомов
            tiles = generate_biome(x, y, biome_type)
            tile_map.extend(tiles)  # Добавляем сгенерированные тайлы в общий список
    return tile_map

