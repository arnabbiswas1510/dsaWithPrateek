"""
N Queens

Given a chess board of N x N , find all ways to place N queens so that they don't each other
"""
def isValid(board, i, j): #This method illustrates usage of 2 variables in for, remember to use zip
    for c in range(j): #Check row upto column
        if board[i][c]:
            return False
    for r,c in zip(range(i,-1,-1), range(j,-1,-1)): #Check upper left diagonal, note this cannot be nested loop else it becomes suduko grid
        #You need to go decreasing i here or it doesnt work
        if board[r][c]:
            return False
    for r,c in zip(range(i, len(board)),range(j,-1,-1)): #Check lower left diagonal, note this cannot be nested loop
        #Start from i here (not i+1) and check how you go decreasing j to 0
        if board[r][c]:
            return False
    return True


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def nQueensSol(board, j):
    if j >= len(board):  #Simple trick to print the last column too
        printBoard(board)
        return True

    for i in range(len(board)): #Remember to loop over rows and the rest is simple backtracking algo
        if isValid(board, i, j):
            board[i][j]=1
            if nQueensSol(board,j+1):
                return True
            board[i][j]=0
    return False

def nQueens(n):
    board=[[0 for i in range(n)] for i in range(n)]
    return nQueensSol(board,0)

if not nQueens(8):
    print("No solution possible")