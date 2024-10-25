import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Settings
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 20
FPS = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font Settings
font = pygame.font.SysFont('Arial', 25)

# Initialize Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Helper Functions
def draw_snake(snake_body):
    """Draw the snake on the screen."""
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def spawn_food(snake_body):
    """Spawn food at a random position within the game grid, avoiding the snake's body."""
    while True:
        food_pos = [random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
                    random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
        if food_pos not in snake_body:
            return food_pos

def show_score(score):
    """Display the current score on the screen."""
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, [0, 0])

def game_over(score):
    """Display the game over message and exit the game."""
    screen.fill(BLACK)
    game_over_text = font.render(f'Game Over! Final Score: {score}', True, RED)
    screen.blit(game_over_text, [WIDTH // 4, HEIGHT // 2])
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main Game Function
def snake_game():
    # Initial Snake and Food Settings
    snake_pos = [[100, 50], [80, 50], [60, 50]]  # Initial snake position (three segments)
    snake_direction = "RIGHT"
    food_pos = spawn_food(snake_pos)
    score = 0

    while True:
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Update Snake Position
        if snake_direction == "UP":
            new_head = [snake_pos[0][0], snake_pos[0][1] - SNAKE_SIZE]
        elif snake_direction == "DOWN":
            new_head = [snake_pos[0][0], snake_pos[0][1] + SNAKE_SIZE]
        elif snake_direction == "LEFT":
            new_head = [snake_pos[0][0] - SNAKE_SIZE, snake_pos[0][1]]
        elif snake_direction == "RIGHT":
            new_head = [snake_pos[0][0] + SNAKE_SIZE, snake_pos[0][1]]
        
        snake_pos.insert(0, new_head)  # Add new head position

        # Check if Snake Eats Food
        if snake_pos[0] == food_pos:
            score += 1
            food_pos = spawn_food(snake_pos)  # Respawn food
        else:
            snake_pos.pop()  # Remove last segment if no food is eaten

        # Check Collisions
        if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT or
            snake_pos[0] in snake_pos[1:]):
            game_over(score)

        # Update Game Display
        screen.fill(BLACK)
        draw_snake(snake_pos)  # Draw the snake
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))  # Draw food
        show_score(score)  # Display current score

        # Refresh Game Screen
        pygame.display.update()

        # Control the Game Speed
        clock.tick(FPS)

# Start the Game
if __name__ == "__main__":
    snake_game()


