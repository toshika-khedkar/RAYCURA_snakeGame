import pygame
import time
import random

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake dimensions
BLOCK_SIZE = 20

# Snake speed and initial length
SNAKE_SPEED = 10
INITIAL_LENGTH = 1

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake function
def snake(block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

# Display current level
def display_level(level):
    font_style = pygame.font.SysFont(None, 25)
    level_text = font_style.render("Level: " + str(level), True, BLACK)
    screen.blit(level_text, [10, 10])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    level = 1
    snake_speed = SNAKE_SPEED
    snake_length = INITIAL_LENGTH

    lead_x = SCREEN_WIDTH // 2
    lead_y = SCREEN_HEIGHT // 2
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []

    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, BLACK)
            screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        # Check if the snake hits the boundary
        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        snake(BLOCK_SIZE, snake_list)
        display_level(level)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        # If the player reaches the required points, move to the next level
        if snake_length - INITIAL_LENGTH >= level * 5:
            level += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop()
