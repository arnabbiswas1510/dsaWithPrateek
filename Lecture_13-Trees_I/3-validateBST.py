"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

from treeOperations import Tree

def isValidBST(root) :
    MIN_VAL = -2**31 - 1
    MAX_VAL = 2**31
    def validateBST(root, low, high):
        if root is None:
            return True
        if root.val <= low or root.val >= high:
            return False
        return (validateBST(root.left, low, root.val) and
                validateBST(root.right, root.val, high))

    return validateBST(root, MIN_VAL, MAX_VAL)

"""
Pre-order
"""
def isValidBSTPre(root):
    stack = [(root, -2**31 - 1, 2**31)] # add the root for validation
    while stack:
        node, low, high = stack.pop()
        if node:
            if (node.val <= low or node.val >= high):
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
    return True

"""
In order
"""

def isValidBSTIn(root):
    stack, cur, prev = [], root, -2**31 - 1
    
    while stack or cur:
        # go down along the left path
        while cur:
            stack.append(cur)
            cur = cur.left

        # no more left subtree, pop a node for processing
        cur = stack.pop()
        if cur.val <= prev:
            return False

        # move to the right subtree of @cur
        prev = cur.val
        cur = cur.right
    return True

t=Tree()
r=t.insertLevelOrder([2,1,3])
print(isValidBST(r))
