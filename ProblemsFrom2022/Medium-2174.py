"""
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

Explanation:

"""
from typing import List


class Solution(object):
    def removeOnes(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.ans = float('inf')
        self.flips = 0
        seen = set()
        def helper():
            flag = False
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 1 and ('r', x) not in seen and ('c', y) not in seen :
                        flag = True
                        seen.add(('r', x))
                        seen.add(('c', y))
                        self.flips+=1
                        helper()
                        self.flips-=1
                        seen.remove(('r', x))
                        seen.remove(('c', y))

            if not flag:
                self.ans=min(self.ans, self.flips)

        helper()
        return self.ans

s = Solution()
print(s.removeOnes([[0,1,0],[1,0,1],[0,1,0]]))
