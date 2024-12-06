import pygame
import sys

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

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Topdown 2D Game")

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

        # Draw rectangles
        for rect in rectangles:
            pygame.draw.rect(screen, GREEN, rect)

        # Draw the circle
        pygame.draw.circle(screen, BLUE, (circle_x, circle_y), CIRCLE_RADIUS)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
