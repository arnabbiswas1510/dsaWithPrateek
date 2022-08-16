"""
https://leetcode.com/problems/diameter-of-binary-tree
"""

ans=-99**99
def diameter(root):
    global ans
    if not root:
        return 0
    left=diameter(root.left)
    right=diameter(root.right)
    if left + right > ans:
        ans = left + right
    return max(left,right)+1

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5])
print(diameter(r))