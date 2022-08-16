"""
https://leetcode.com/problems/binary-tree-coloring-game

Explanation: https://www.youtube.com/watch?v=DIXDTh-aOQ4
Main intution is that the strategy to win is to block immediate neighbor (left, right or parent) with max nodes
You win the game if max(left_nodes, right_nodes, parent_nodes) > n/2. Parent_nodes = n - left - right -1(for self)
"""
from treeOperations import Node
class Solution:
    def btreeGameWinningMove(self,root:Node, n:int, x:int) -> bool:
        def countNode(cur): #Standard way to count nodes in tree using DFS
            if not cur:
                return 0
            left = countNode(cur.left)
            right = countNode(cur.right)

            return left + right +1

        def findX(cur):
            nonlocal left_nodes, right_nodes #nonlocal behaves same as global, except it is used in nested functions
            #global keyword must be used if you want to modify a global variable. Without global u can only read
            if not cur:
                return

            if cur.val == x:
                left_nodes = countNode(cur.left)
                right_nodes = countNode(cur.right)
                return

            left=findX(cur.left)
            right=findX(cur.right)

        left_nodes = right_nodes = parent_nodes = 0

        findX(root)

        parent_nodes = n - left_nodes - right_nodes -1

        return max(left_nodes, right_nodes, parent_nodes) > n/2

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5,6,7,8,9,10,11])
s=Solution()
print(s.btreeGameWinningMove(r,11,3))