"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree

"""
def goodNodes(root, maximum):
    if not root:
        return 0
    maximum=max(maximum, root.val)
    if root.val == maximum: #Why is this not >= ?
        return 1+ goodNodes(root.left, maximum) + goodNodes(root.right, maximum)
    else:
        return goodNodes(root.left, maximum) + goodNodes(root.right, maximum)

def goodNodesDoesntWork(root): #Can you intuit why?
    count=0
    for child in filter(None, [root.left, root.right]): #Filter out nulls
        count += child.val >= root.val
        child.val = max(child.val, root.val)
        goodNodesDoesntWork(child)
    return count + 1

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([3,1,4,3,None,1,5])
print(goodNodesDoesntWork(r))