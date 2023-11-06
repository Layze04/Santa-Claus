import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SANTA_SIZE = 100
FPS = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Santa Claus Dance")

# Load Santa Claus image
santa_img = pygame.image.load("santa.png")
santa_img = pygame.transform.scale(santa_img, (SANTA_SIZE, SANTA_SIZE))

# Get the rect of Santa Claus
santa_rect = santa_img.get_rect()

# Initial position
santa_rect.center = (WIDTH // 2, HEIGHT // 2)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Santa Claus randomly
    santa_rect.move_ip(random.randint(-5, 5), random.randint(-5, 5))

    # Check boundaries
    if santa_rect.left < 0:
        santa_rect.left = 0
    elif santa_rect.right > WIDTH:
        santa_rect.right = WIDTH
    if santa_rect.top < 0:
        santa_rect.top = 0
    elif santa_rect.bottom > HEIGHT:
        santa_rect.bottom = HEIGHT

    # Clear the screen
    screen.fill(WHITE)

    # Draw Santa Claus
    screen.blit(santa_img, santa_rect)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
