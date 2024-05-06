"""
https://leetcode.com/problems/max-area-of-island/

Explanation:

"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Almost similar to the famous number of islands problem on LeetCode.
        # We'll loop over all the elements of the grid.
        # If the element value is 1, that element is a part of some island.
        # We find the extent of that island by performing dfs starting from that node.ArithmeticError
        # While doing that, we set the element values to 0 to indicate that we've already visited that element,
        # and we return the area of island traversed till now.

        def dfs(i, j):
            # Base condition: If we reach the end of the grid, or if the element value is zero,
            # then we've reached the end of the island in that directions. Hence, we return 0
            if((i < 0) or (i >= numRows) or
                    (j < 0) or (j >= numCols) or
                    (not grid[i][j])):
                return 0
            # Mark the element visited by changing its value to 0.
            grid[i][j] = 0
            # Call DFS recursively on four sides.
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        numRows, numCols = len(grid), len(grid[0])
        maxArea = 0
        for i in range(numRows):
            for j in range(numCols):
                if(grid[i][j]):
                    area = dfs(i, j)
                    if(area > maxArea):
                        maxArea = area
        return maxArea

s = Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                         [0,0,0,0,0,0,0,1,1,1,0,0,0],
                         [0,1,1,0,1,0,0,0,0,0,0,0,0],
                         [0,1,0,0,1,1,0,0,1,0,1,0,0],
                         [0,1,0,0,1,1,0,0,1,1,1,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,0],
                         [0,0,0,0,0,0,0,1,1,1,0,0,0],
                         [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
