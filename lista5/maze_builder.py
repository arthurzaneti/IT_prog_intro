# python 3

import random

def generate_maze(m, n, room = 0, wall = 1, cheese = '.' ):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Directions: (row_offset, col_offset) for N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        """Recursive DFS to generate the maze."""
        # Mark the current cell as visited by making it a path (room)
        maze[2 * x + 1][2 * y + 1] = room

        # Shuffle the directions to create a random path
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # New cell coordinates
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                print_maze(maze)
                # Open the wall between the current cell and the new cell
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                # Recursively visit the new cell
                dfs(nx, ny)

    # Start DFS from the top-left corner (0, 0) of the logical grid
    dfs(0, 0)
    count = 0
    while True: # placing the chesse
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        count += 1
        if maze[i][j] == room:
            maze[i][j] = cheese 
            break

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == '__main__':
    m, n = 5, 7  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)

    room = ' '
    wall = 'H'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)