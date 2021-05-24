"""
Very intuitive logic. Keep top, downleft,right pointers and direction value as computed below
iteratively using modulo. The below logic
"""
def spiralMatrix(mat):
    top, down, left, right = 0, len(mat), 0, len(mat[0])
    dir = 0 # 0=right, 1 = down, 2 = left, 3= up
    while top < down and left < right:
        #4 lines of code below repeat for each if (direction of traveral)
        if dir == 0: #go left
            for i in range(left, right):
                print(mat[top][i], end=",") #print top row
            top+=1 #lower top
        if dir == 1: #go down
            for i in range(top,down):
                print(mat[i][right-1], end=",") #print right column
            right-=1 #move right towards left
        if dir == 2: #go left
            for i in range(right-1, left-1, -1):
                print(mat[down-1][i], end=",") #print bottom row
            down-=1 #Move down up
        if dir == 3: #go up
            for i in range(down-1,top-1,-1):
                print(mat[i][left], end=",") #print left row
            left+=1 #Move left up
        dir = (dir+1)%4


mat = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]]

print(spiralMatrix(mat))
