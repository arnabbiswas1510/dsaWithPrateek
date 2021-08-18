"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Explanation: https://www.youtube.com/watch?v=13m9ZCB8gjw
"""

def lca(root, p, q):
    if not root:
        return None
    if root.val == p or root.val ==q:
        return root
    left=lca(root.left, p, q)
    right=lca(root.right, p, q)
    if left and right:
        return root
    if not(left or right):
        return None
    return left if left else right

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([3,5,1,6,2,0,8,None,None,7,4])
res=lca(r,5,1)
print(res.val if res else None)