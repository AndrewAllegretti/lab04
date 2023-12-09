from Stack import Stack


def solveMaze(maze, startX, startY):
    path = Stack()
    x = startX
    y = startY
    steps = 1
    path.push([x, y])
    maze[x][y] = steps
    steps += 1
    while maze[x][y] != 'G':
        
        if maze[x - 1][y] == ' ' or maze[x - 1][y] == 'G':  # NORTH
            x -= 1
            path.push([x, y])
            if maze[x][y] == 'G':
                return True
            maze[x][y] = steps
            steps += 1
        elif maze[x][y-1] == ' ' or maze[x][y-1] == 'G':  # WEST
            y -= 1
            path.push([x, y])
            if maze[x][y] == 'G':
                return True
            maze[x][y] = steps
            steps += 1
        elif maze[x +1][y] == ' ' or maze[x + 1][y] == 'G':  # SOUTH
            x += 1
            path.push([x, y])
            if maze[x][y] == 'G':
                return True
            maze[x][y] = steps
            steps += 1
        elif maze[x][y + 1] == ' ' or maze[x][y + 1] == 'G':  # EAST
            y += 1
            path.push([x, y])
            if maze[x][y] == 'G':
                return True
            maze[x][y] = steps
            steps += 1
        else:
            if path.isEmpty():
                return False
            else:
                path.pop()
                if path.isEmpty():
                    return False
                else:
                    x,y = path.peek()[0],path.peek()[1]

    return True



def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='', end='')
        print("|")
    return
