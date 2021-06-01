"""
Traverse a matrix using recursion
"""

def traverse(mat,i,j):
    rows=len(mat)
    cols=len(mat[0])
    if i >= rows or j >= cols:
        return
    if mat[i][j] == -1:
        return
    print(mat[i][j], end=" ")
    mat[i][j]=-1
    traverse(mat,i+1,j)
    traverse(mat,i,j+1)


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
traverse(mat,0,0)