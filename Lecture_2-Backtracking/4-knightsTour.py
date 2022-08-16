"""
Knights Tour

Print the steps taken by a Knight to move through an N by N board
"""

def isValid(board,row, col):
    if row >=0 and row <len(board) and col >= 0 and col < len(board) and board[row][col]==-1:
        return True
    return False

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def knightTour(board,currRow,currCol,n):
    if n == len(board)**2:
        printBoard(board)
        return True

    for i in range(len(board)):
        newRow=currRow+nextRow[i]
        newCol=currCol+nextCol[i]
        if isValid(board,newRow,newCol):
            board[newRow][newCol]=n
            if knightTour(board,newRow,newCol,n+1):
                return True
            board[newRow][newCol]=-1
    return False

n=8
nextRow=[1,2,2,1,-1,-2,-2,-1]
nextCol=[2,1,-1,-2,-2,-2,-1,1,2]
board=[[-1 for i in range(n)] for i in range(n)]
board[0][0]=0
knightTour(board,0,0,1) #Remember to start with 1 and initialize starting position to 0
#Else the last square will remain empty