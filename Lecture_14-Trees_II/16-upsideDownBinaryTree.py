"""
https://kennyzhuang.gitbooks.io/leetcode-lock/content/156_binary_tree_upside_down.html

Explanation: https://www.youtube.com/watch?v=JjaJQi77984
 
"""
from treeOperations import Node
class Solution:
    def upsideDownBinaryTree(self,root:Node) -> Node:
        def dfs(cur): #Remember 90% of tree problems use DFS
            if not cur.left: #Get to the left most node and return that as newRoot
                return cur
            newRoot = dfs(cur.left)
            #Now rearrange the pointers as shown in video
            cur.left.left = cur.right
            cur.left.right = cur
            cur.left = None
            cur.right = None

            return newRoot
        if not root: #Boundary
            return None

        return dfs(root)

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5])
s=Solution()
r=s.upsideDownBinaryTree(r)
t.printLevelOrder(r)