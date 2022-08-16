"""
https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1650-lowest-common-ancestor-of-a-binary-tree-iii

Same problem but here the node has a parent, so much simpler than previous
"""

def find(node, val):
    if node:
        if node.val == val:
            return node
        ret = find(node.left, val)
        if ret:
            return ret
        return find(node.right, val)

def lca3(p,q):
    a,b=p,q
    while a and b and a.val != b.val:
        a = a.parent if a else q
        b = b.parent if b else p
    return a.val if a else None

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([3,5,1,6,2,0,8,None,None,7,4])
print(lca3(find(r,5), find(r,4)))