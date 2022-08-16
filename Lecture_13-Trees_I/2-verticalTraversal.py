"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

from collections import defaultdict
from collections import deque
from treeOperations import Tree

def verticalTraversal(arr):
    tree=Tree()
    root=tree.insertLevelOrder(arr)
    if root == None:
        return []

    columnTable = defaultdict(list)
    parent = deque([(root, 0, 0)])

    while parent:
        node, row, column = parent.popleft()
        columnTable[column].append((row, node.val))
        if node.left:
            parent.append((node.left,row+1, column-1))
        if node.right:
            parent.append((node.right,row+1, column+1))
    # Here, the columnTable is a dictionary, where the key is column number,
    # And for values, is a list, each element E is a tuple,  E[0] is row numebr, E[1] is node.val
    # First, sort by column, then sort by row, if has the same row, we compare the node.val
    return [[row_sort[1]for row_sort in sorted(columnTable[column])]for column in sorted(columnTable)]

print(verticalTraversal([3,9,20,None,None,15,7]))
