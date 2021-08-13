"""
https://leetcode.com/problems/path-sum/
"""
def hasPathSum(root, target):
    if root:
        if not (root.left or root.right) and target == root.val:
            return True
    return (root.left and hasPathSum(root.left, target-root.val)) \
           or (root.right and hasPathSum(root.right, target-root.val))

#Prateek's simpler version but doesnt work when sum is not present
def hasPathSum2(root, target):
    if not root:
        return 0
    return hasPathSum2(root.left, target-root.val) or hasPathSum2(root.right, target-root.val)

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([5,4,8,11,None,13,4,7,2,None,None,None,1])
print(hasPathSum(r,22))