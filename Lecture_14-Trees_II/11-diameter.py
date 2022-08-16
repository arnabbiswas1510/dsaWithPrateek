"""
https://leetcode.com/problems/diameter-of-binary-tree

Explanation: https://www.youtube.com/watch?v=ey7DYc9OANo
n a tree, #nodes = #edges+1.

"""

def height(root):
    if not root:
        return 0
    hleft=height(root.left)
    hright=height(root.right)
    return max(hleft,hright)+1


def diameter(root):
    if not root:
        return 0
    hleft=height(root.left)
    hright=height(root.right)
    dleft=diameter(root.left)
    dright=diameter(root.right)
    return max(hleft+hright+1, dleft, dright)

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5,None,6,7,8])
print(diameter(r))