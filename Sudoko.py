import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 540, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont("Arial", 40)

# Sudoku Puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class SudokuGrid:
    def __init__(self, board):
        self.board = board
        self.selected = None
        self.temp_value = None

    def draw_grid(self):
        """Draws the Sudoku grid with numbers."""
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(SCREEN, BLACK, (0, i * 60), (540, i * 60), line_width)
            pygame.draw.line(SCREEN, BLACK, (i * 60, 0), (i * 60, 540), line_width)

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    value = FONT.render(str(self.board[row][col]), True, BLACK)
                    SCREEN.blit(value, (col * 60 + 20, row * 60 + 15))

    def place_number(self, value):
        """Place a number in the selected cell."""
        row, col = self.selected
        if self.board[row][col] == 0:
            self.board[row][col] = value

    def select_cell(self, row, col):
        """Select a cell based on grid position."""
        self.selected = (row, col)

    def clear_cell(self):
        """Clear the selected cell."""
        row, col = self.selected
        if self.board[row][col] != 0:
            self.board[row][col] = 0

def draw_selected_cell(selected):
    """Highlight the selected cell."""
    if selected:
        row, col = selected
        pygame.draw.rect(SCREEN, BLUE, (col * 60, row * 60, 60, 60), 3)

def main():
    grid = SudokuGrid(sudoku_board)
    running = True
    key = None

    while running:
        SCREEN.fill(WHITE)
        grid.draw_grid()

        draw_selected_cell(grid.selected)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks to select cells
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // 60, pos[0] // 60
                grid.select_cell(row, col)

            # Handle keyboard inputs for number keys
            if event.type == pygame.KEYDOWN:
                if grid.selected:
                    if event.key == pygame.K_1: key = 1
                    elif event.key == pygame.K_2: key = 2
                    elif event.key == pygame.K_3: key = 3
                    elif event.key == pygame.K_4: key = 4
                    elif event.key == pygame.K_5: key = 5
                    elif event.key == pygame.K_6: key = 6
                    elif event.key == pygame.K_7: key = 7
                    elif event.key == pygame.K_8: key = 8
                    elif event.key == pygame.K_9: key = 9
                    elif event.key == pygame.K_DELETE:
                        grid.clear_cell()

        if grid.selected and key is not None:
            grid.place_number(key)
            key = None

        pygame.display.update()

if __name__ == "__main__":
    main()
