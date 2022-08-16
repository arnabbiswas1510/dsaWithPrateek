"""
https://leetcode.com/problems/range-sum-of-bst
"""

def rangeSumBST(root, L, R):
    if not root: #base case
        return 0
    if root.val < L: #exclude left branch
        return rangeSumBST(root.right, L, R)
    if root.val > R: #exclude right branch
        return rangeSumBST(root.left, L, R)
    return root.val + rangeSumBST(root.right, L, R) + rangeSumBST(root.left, L, R)

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([10,5,15,3,7,None,18])
print(rangeSumBST(r,7,15))