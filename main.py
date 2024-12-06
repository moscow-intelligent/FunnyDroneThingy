import pygame
import sys
from classes import World, Tile, Tiles
# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RECT_SIZE = 50
CIRCLE_RADIUS = 15
FPS = 60

# Colors
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

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

    # Create a grid of rectangles (12 rows x 16 columns)
    rectangles = create_rectangles(12, 16)

    # Set up font for displaying coordinates
    font = pygame.font.Font(None, 36)
    w = World()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            circle_x -= 5
        if keys[pygame.K_RIGHT]:
            circle_x += 5
        if keys[pygame.K_UP]:
            circle_y -= 5
        if keys[pygame.K_DOWN]:
            circle_y += 5

        # Fill the screen with white
        screen.fill(WHITE)

        # Calculate the camera offset
        camera_x = circle_x - SCREEN_WIDTH // 2
        camera_y = circle_y - SCREEN_HEIGHT // 2

        # Draw rectangles with camera offset

        for rect in rectangles:
            # Offset the rectangle's position based on the camera
            offset_rect = rect.move(-camera_x, -camera_y)
            pygame.draw.rect(screen, GREEN, offset_rect)

        for t in w.tiles:
            t.rect = t.move(-camera_x, -camera_y)
            t.draw(screen)
        # Draw the circle at the center of the screen
        pygame.draw.circle(screen, BLUE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), CIRCLE_RADIUS)

        # Render the coordinates
        coordinates_text = f"Coordinates: ({circle_x}, {circle_y})"
        text_surface = font.render(coordinates_text, True, BLACK)
        screen.blit(text_surface, (10, 10))  # Draw text at (10, 10)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
