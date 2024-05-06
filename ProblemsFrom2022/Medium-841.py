"""
https://leetcode.com/problems/keys-and-rooms/

Explanation:
Performs Iterative DFS using Stack

"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms):
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
        return len(seen) == len(rooms)

s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
