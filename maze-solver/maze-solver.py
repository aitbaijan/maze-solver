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
    
    if maze[x][y] == '#' or (x, y) in path:
        return False

    path.append((x, y))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if find_path(maze, nx, ny, path, rows, cols):
                return True
    
    path.pop()
    return False

def display_maze(maze, path=None):
    if path:
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '.'
                

    for row in maze:
        print(' '.join(row))


def main():

    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    maze = generate_maze(rows, cols)

    path = []
    if find_path(maze, 0, 0, path, rows, cols):
        print("\nПуть найден!")
        display_maze(maze, path)
    else:
        print("\nПуть не найден!")
        display_maze(maze)

if __name__ == "__main__":
    main()