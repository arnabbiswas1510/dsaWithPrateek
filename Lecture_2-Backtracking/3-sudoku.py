"""
Sudoku

Solve the Sudoku
"""
import math

def isValid(board,i, j, n):
    for x in range(len(board)): #Check row upto column
        if board[i][x] == n or board[x][j] == n:
            return False
    #This will need to be remembered:
    root = int(math.sqrt(len(board)))
    startRow = i - i%root #Get to 6 if u are 8
    startCol = j - j%root
    for r in range(root):
        for c in range(root):
            if board[r+startRow][c+startCol]==n:
                return False
    return True

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def sudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]) == 0:
                break
        else:
            continue
        break  # Pythonic way for if break happens in inner loop, break outer loop too.
    if i == len(board)-1 and j == len(board)-1:
        printBoard(board)
        return True

    for n in range(1,len(board)+1):
        if isValid(board,i, j, n):
            board[i][j]=n
            if sudoku(board):
                return True
            board[i][j]=0
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
sudoku(grid)