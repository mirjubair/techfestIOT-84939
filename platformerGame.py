import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen and clock
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")
CLOCK = pygame.time.Clock()

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = BLUE
PLAYER_SPEED = 5
JUMP_POWER = 15
GRAVITY = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel_x = 0
        self.vel_y = 0
        self.jumping = False

    def update(self):
        # Gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:  # Limit falling speed
            self.vel_y = 10

        # Movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Boundary checks
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel_y = -JUMP_POWER

    def move(self, dx):
        self.vel_x = dx

    def stop(self):
        self.vel_x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

# Game setup
player = Player()

# Platforms
platforms = pygame.sprite.Group()
initial_platform = Platform(0, HEIGHT - 50, WIDTH, 50)  # Ground platform
platform1 = Platform(300, 400, 200, 20)
platform2 = Platform(500, 300, 150, 20)
platforms.add(initial_platform, platform1, platform2)

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(platforms)

def game_loop():
    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(-PLAYER_SPEED)
                if event.key == pygame.K_RIGHT:
                    player.move(PLAYER_SPEED)
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()

        # Update
        all_sprites.update()

        # Check for collision between player and platforms
        if player.vel_y > 0:  # Falling downwards
            hits = pygame.sprite.spritecollide(player, platforms, False)
            if hits:
                player.rect.bottom = hits[0].rect.top
                player.vel_y = 0
                player.jumping = False

        # Drawing
        SCREEN.fill(WHITE)
        all_sprites.draw(SCREEN)
        pygame.display.flip()

if __name__ == "__main__":
    game_loop()
