"""
Maze problem

Given a matrix of 0s and 1s, Print all possible paths from Source to Destination. You can move in 8 directions. (up, down, left right and other 4 diagonals).
"""
#This solution just prints one path. We need to modify this solution to print all possible paths

def isValid(maze, i, j):
    return i >=0 and i < len(maze) and j>=0 and j < len(maze[0])

def mazeSol(maze, i, j, sol):
    if i == len(maze)-1 and j == len(maze[0]) -1:
        sol[i][j]=1 #Can you return sol here? Never works due to stack unwind
        return True

    if isValid(maze, i, j):
        if maze[i][j] == 0:
            sol[i][j] =0
            return False

        sol[i][j]=1
        if mazeSol(maze, i+1, j, sol) == True:
            return True #The reason that it doesnt print all paths is that you return from here as soon as you find a single path

        if mazeSol(maze, i, j+1, sol) == True:
            return True

        if mazeSol(maze, i-1, j, sol) == True:
            return True

        if mazeSol(maze, i, j-1, sol) == True:
            return True

        sol[i][j]=0
        return False



def solveMaze(maze):
    rows = len(maze)
    cols = len(maze[0])
    sol=[[0 for i in range(cols)] for i in range(rows)]
    mazeSol(maze,0,0,sol)
    for i in range(rows):
        for j in range(cols):
            print(sol[i][j], end= " ")
        print()

if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 1, 0],
            [1, 1, 1]]

    solveMaze(maze)

"""
Maze problem - print all paths
"""
def isValid(maze, i, j):
    return i >=0 and i < len(maze) and j>=0 and j < len(maze[0])

def mazeSol2(maze, i, j, paths):
    if i == len(maze)-1 and j == len(maze[0]) -1:
        paths.append(maze[i][j])
        print(paths)
        paths.pop()  #Why here? This context is not retained in the call stack right?
        return

    if isValid(maze, i, j):
        if maze[i][j] == 0:
            #paths.pop()  This makes sense. We dont need to pop the last added cell if the new one is 0
            return

        paths.append(maze[i][j])
        mazeSol2(maze, i+1, j, paths)

        mazeSol2(maze, i, j+1, paths)
        paths.pop()
        #return  Do we ever need a return from the last line in a recursive function?

maze = [['A', 'B', 'C'],
        ['D', 0, 'J'],
        ['F', 'G', 'H']]

mazeSol2(maze,0,0,[])