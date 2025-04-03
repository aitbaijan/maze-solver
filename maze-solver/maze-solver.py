import random

def generate_maze(rows, cols):
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    

    def carve_path(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 < nx < rows - 1 and 0 < ny < cols - 1 and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx // 2][y + dy // 2] = ' '  
                carve_path(nx, ny)

   
    maze[1][1] = ' '
    carve_path(1, 1)

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    
    return maze

def find_path(maze, x, y, path, visited):
    rows, cols = len(maze), len(maze[0])

    
    if maze[x][y] == 'E':
        path.append((x, y))
        return True

    
    if maze[x][y] == '#' or (x, y) in visited:
        return False

    visited.add((x, y))
    path.append((x, y))

    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if find_path(maze, nx, ny, path, visited):
                return True

    path.pop()  
    return False

def display_maze(maze, path=None):
    if path:
        for x, y in path:
            if maze[x][y] not in ('S', 'E'):
                maze[x][y] = '.'


    for row in maze:
        print(' '.join(row))


def main():

    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    if rows < 5 or cols < 5:
        print("Размеры лабиринта должны быть не менее 5x5!")
        return

    maze = generate_maze(rows, cols)

    path = []
    
    if find_path(maze, 0, 0, path, set()):
        print("\nПуть найден!")

    else:
        print("\nПуть не найден!")

    display_maze(maze, path)

if __name__ == "__main__":
    main()