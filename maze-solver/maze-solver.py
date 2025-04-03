import random

def generate_maze(rows, cols):
    start = (0, 0)
    end = (rows - 1, cols - 1)

    maze = [['#' for _ in range(cols)] for _ in range(rows)]

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    def carve_path(x, y):
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)