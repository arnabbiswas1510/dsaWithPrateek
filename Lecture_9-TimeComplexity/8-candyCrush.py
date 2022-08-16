"""
https://just4once.gitbooks.io/leetcode-notes/content/leetcode/two-pointers/723-candy-crush.html

"""
def printMat(mat):
    if mat:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=' ')
            print()

def candyCrush(board):
    r, c = len(board) , len(board[0])
    crush = False
    for i in range(r):
        for j in range(c):
            #check horizontal line
            v = abs(board[i][j])
            if (v == 0):
                continue
            if j + 2 < c and v == abs(board[i][j + 1]) and v == abs(board[i][j + 2]):
                crush = True
                board[i][j] = board[i][j + 1] = board[i][j + 2] = -v
            #check vertical line
            if i + 2 < r and v == abs(board[i + 1][j]) and v == abs(board[i + 2][j]):
                crush = True
                board[i][j] = board[i + 1][j] = board[i + 2][j] = -v

    #crush candy
    for j in range(c):
        id = r - 1;
        for i in range(r-1,-1,-1):
            if (board[i][j] > 0):
                board[id][j] = board[i][j]
                id-=1
        while (id >= 0):
            board[id][j] = 0
            id-=1
    ret= candyCrush(board) if crush else board
    return printMat(ret)

print(candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))