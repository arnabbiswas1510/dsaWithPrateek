"""
https://leetcode.com/problems/invert-binary-tree/

Simple trick in this problem is to set invertTree(root.left) as the new right node and likewise for the new left node
"""

def invertTree(root):
    if not root:
        return root;
    r = invertTree(root.left)
    l = invertTree(root.right)
    root.right=r #set invertTree(root.left) as the new right node
    root.left=l
    return root

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([4,2,7,1,3,6,9])
r=(invertTree(r))
t.printLevelOrder(r)