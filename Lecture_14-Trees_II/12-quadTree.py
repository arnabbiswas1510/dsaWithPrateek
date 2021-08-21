"""
https://leetcode.com/problems/construct-quad-tree/

Youtube the concept of Quad tree and pay attention to how a leaf is determined. Quad trees are used in programming games
"""

class QuadNode:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        n = len(grid)

        def is_leaf(l, r, t, b) -> bool: #Coordinates of cell are provided by t and l. r and b are just used to
            # calculate rowlen and num rows to iterate for the current quadrant
            val, rowLen = grid[t][l], r - l

            for row in range(t, b):
                #Its a leaf if it is all 0s or 1s for each row in the current quadrant
                if sum(grid[row][l:r]) != rowLen * val:
                    return (0, val)

            return (1, val)

        #Remember the signature of this and the isLeaf method (same signature). The implmentation os this method is
        # intuitive DFS
        def construct_tree(l, r, t, b):
            isLeafNode, val = is_leaf(l, r, t, b)
            if isLeafNode: return QuadNode(val, 1, None, None, None, None)

            mid_row, mid_col = l + (r - l) // 2, t + (b - t) // 2
            topLeft = construct_tree(l, mid_row, t, mid_col)
            topRight = construct_tree(mid_row, r, t, mid_col)
            bottomLeft = construct_tree(l, mid_row, mid_col, b)
            bottomRight = construct_tree(mid_row, r, mid_col, b)

            return QuadNode(val, 0, topLeft, topRight, bottomLeft, bottomRight)

        return construct_tree(0, n, 0, n)

grid=[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
s=Solution()
n=s.construct(grid)
print(n)