import pygame
import sys
from classes import World, Tile, Tiles, Player, TestEntity, ActiveProvider, PlayerDraw
from mapgen import generate_map
from config import *
from json import loads, dumps
from networking.client import *
pygame.init()

# Constants


# Colors
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Logistic bot sim UwU")

# Circle position
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2

# Create a grid of rectangles
def create_rectangles(rows, cols):
    rectangles = []
    for row in range(rows):
        for col in range(cols):
            rect_x = col * RECT_SIZE
            rect_y = row * RECT_SIZE
            rectangles.append(pygame.Rect(rect_x, rect_y, RECT_SIZE, RECT_SIZE))
    return rectangles

# Main game loop
def main():
    global circle_x, circle_y
    clock = pygame.time.Clock()
    # NETWORK
    net = GameClient("ws://localhost:8765")
    net.run()
    # Create a grid of rectangles (12 rows x 16 columns)
    rectangles = create_rectangles(12, 16)
    my_name = input("Enter name")
    # Set up font for displaying coordinates
    font = pygame.font.Font(None, 36)
    w = World()
    p = Player(0, 0, 10)
    pd = PlayerDraw(0,0, my_name)
    #map = [[Tile(0, 0, Tiles.WATER)]]
    ent = ActiveProvider(100, 100)
    entities = pygame.sprite.Group()
    entities.add(ent)
    rq_queue = []
    i = 0
    while True:
        i +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        p.move(keys)
        screen.fill(WHITE)
        camera_x = p.x - SCREEN_WIDTH // 2
        camera_y = p.y - SCREEN_HEIGHT // 2
        if ent.rect.x <= p.x <= ent.rect.x + 64 and ent.rect.y <= p.y <= ent.rect.y + 64:
            pygame.draw.circle(screen, RED, (250, 100), CIRCLE_RADIUS)
        # Draw rectangles with camera offset
        # TEST GREEN RECTANGLES
        for rect in rectangles:
            # Offset the rectangle's position based on the camera
            offset_rect = rect.move(-camera_x, -camera_y)
            pygame.draw.rect(screen, GREEN, offset_rect)

        # for m in map:
        #     for t in m:
        #         t.rect = t.move(-camera_x, -camera_y)
        #         t.draw(screen)

        for e in entities:
            e.draw(screen, camera_x, camera_y)
        # Draw the circle at the center of the screen

        pygame.draw.circle(screen, BLUE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), CIRCLE_RADIUS)

        # Render the coordinates
        coordinates_text = f"Coordinates: ({p.x}, {p.y})"
        text_surface = font.render(coordinates_text, True, BLACK)
        screen.blit(text_surface, (10, 10))  # Draw text at (10, 10)
        fps = clock.get_fps()  # Get the current FPS

        fps_text = font.render(f"FPS: {fps:.2f}", True,BLACK)  # Render the FPS text

        screen.blit(fps_text, (10, 100))  # Draw the FPS text at position (10, 10)
        #NETWORK
        for player in net.cords:
            if player != my_name:
                pd = PlayerDraw(net.cords[player][0], net.cords[player][1], player)
                pd.draw(screen, camera_x, camera_y)
        net.send_coordinates((p.x, p.y), my_name)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
