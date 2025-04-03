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

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
        
            if 0 < nx < rows - 1 and 0 < ny < cols - 1 and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                carve_path(nx, ny)

    
    carve_path(1, 1)
    return maze

def find_path(maze, x, y, path, rows, cols):
    if (x, y) == (rows - 1, cols - 1):
        path.append((x, y))
        return True
    
    if 0 <= x < rows and 0 <= y < cols and maze[x][y] == ' ':

        maze[x][y] = '.'
        path.append((x, y))

    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if find_path(maze, x + dx, y + dy, path, rows, cols):
                return True
        
    
        path.pop()
        maze[x][y] = ' '
    
    return False

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

        def main():
            rows = int(input("Введите количество строк лабиринта: ") or 10)
            cols = int(input("Введите количество столбцов лабиринта: ") or 10)

    maze = generate_maze(rows, cols)
    path = []
    find_path(maze, 0, 0, path, rows, cols)

    print("\nЛабиринт с решением:")
    print_maze(maze)
    print("\nПуть к выходу:")
    print(path)

if name == "__main__":
    main()