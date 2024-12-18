import os
import random
import time
import platform

def clear_console():
    """Clears the console based on the operating system."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_board(width, height):
    """Generates a board with random initial live and dead cells."""
    return [[1 if random.random() < 0.5 else 0 for _ in range(width)] for _ in range(height)]

def copy_board(board):
    """Creates a deep copy of the board."""
    return [row[:] for row in board]

def get_life_cell(board, x, y):
    """Counts the number of live neighbors for a cell at position (x, y)."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    rows, cols = len(board), len(board[0])

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 1:
            count += 1

    return count

def game_of_life(board):
    """Applies Conway's rules to generate the next board state."""
    rows, cols = len(board), len(board[0])
    new_board = copy_board(board)

    for x in range(rows):
        for y in range(cols):
            live_neighbors = get_life_cell(board, x, y)
            if board[x][y] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[x][y] = 0  # Dies
            else:  # Dead cell
                if live_neighbors == 3:
                    new_board[x][y] = 1  # Becomes live

    return new_board

def render(board):
    """Prints the board to the console."""
    for row in board:
        print("".join("*" if cell == 1 else " " for cell in row))
    print()

def run_game(width, height, delay=0.5):
    """Runs Conway's Game of Life."""
    board = get_board(width, height)
    try:
        while True:
            render(board)
            time.sleep(delay)
            clear_console()
            board = game_of_life(board)
    except KeyboardInterrupt:
        print("Game stopped.")

# Example usage
if __name__ == "__main__":
    run_game(50, 50, 0.5)
