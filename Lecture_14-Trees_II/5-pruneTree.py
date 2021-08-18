"""
https://leetcode.com/problems/binary-tree-pruning

This one is tricky, but logic is very intuitive and fluid
https://www.youtube.com/watch?v=77LJc56bwnE
"""

def pruneTree(root):
    if not root:
        return None
    left_valid = pruneTree(root.left)
    right_valid = pruneTree(root.right)
    if not left_valid:
        root.left=None
    if not right_valid:
        root.right=None
    return root.val == 1 or left_valid or right_valid

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,1,0,1,1,0,1,0])
pruneTree(r)
t.printLevelOrder(r)