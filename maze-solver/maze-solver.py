import random

def generate_maze(rows, cols):
    start = (0, 0)
    end = (rows - 1, cols - 1)

    maze = [['#' for _ in range(cols)] for _ in range(rows)]