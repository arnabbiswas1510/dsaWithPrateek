"""
Rotate a matrix by 90 degree in clockwise direction without using any extra space
Difficulty Level : Medium

Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Examples:

Input:
1 2 3
4 5 6
7 8 9
Output:
7 4 1
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2
"""

"""
The challenge in this problem is to rotate a matrix without overwriting the numbers as you rotate.

So use the below strategy:

Consider matrix:

1 2 3
4 5 6
7 8 9

1. Transpose - swap(m[i][j], m[j][i]). This yields

1 4 7
2 5 8
3 6 9

ie the rows and columns have interchanged

2. Then flip vertically is swap(m[i][j], m[i][len-j]), This yields

7 4 1
8 5 2
9 6 3

or the rotated matrix
"""

def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print()
        

mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]


def rotate(mat):
    l=len(mat) #This approach only works for square matrix where len of rows and cols is the same
    #Note logic of both nested loops below
    #First transpose
    for i in range(l):
        for j in range(i,l): #Note that j starts from i here and hence this is not O(n^2)
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    #Then flip vertically
    for i in range(l):
        for j in range(l//2):
            mat[i][j],mat[i][l-j-1] =mat[i][l-j-1],mat[i][j] #Only change columns, you also need l-1 here to
            # prevent outofbounds exception

rotate(mat)
printMat(mat)
