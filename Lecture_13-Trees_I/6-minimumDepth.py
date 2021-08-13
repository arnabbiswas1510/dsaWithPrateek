"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

def minDepth(root):
    if not root:
        return 99**99
    elif not root.left and not root.right: #Return 1 if leaf reached
        return 1
    else:
        return 1+min(minDepth(root.left), minDepth(root.right))

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([2,None,3,None,4,None,5,None,6]) #Doesnt work for this case should return 5
#r=t.insertLevelOrder([3,9,20,None,None,15,7])
print(minDepth(r))