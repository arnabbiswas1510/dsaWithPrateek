"""
https://leetcode.com/problems/symmetric-tree/
"""
def isSymmetric(root) :
    def isSymmetric(t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None or t1.val != t2.val: #Note how this is done
            return False
        return (isSymmetric(t1.left, t2.right) and
                isSymmetric(t1.right, t2.left))

    return isSymmetric(root.left, root.right)

from treeOperations import Tree

t=Tree()
r=t.insertLevelOrder([1,2,2,None,3,None,3])
print(isSymmetric(r))
