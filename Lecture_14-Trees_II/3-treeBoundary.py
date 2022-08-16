"""
https://xiaoguan.gitbooks.io/leetcode/content/LeetCode/545-boundary-of-binary-tree-medium.html
"""

def isLeaf(root):
    return not(root.left or root.right)

def addLeaves(root, res):
    if isLeaf(root):
        res.append(root.val)
        return
    if(root.left):
        addLeaves(root.left, res)
    if(root.right):
        addLeaves(root.right, res)

def treeBoundary(root):
    if not root:
        return
    res=[]
    #First add self
    if not isLeaf(root):
        res.append(root.val)
    #Then add left boundary
    cur=root.left
    while cur:
        if not isLeaf(cur):
            res.append(cur.val)
        if cur.left:
            cur=cur.left
        else:
            cur=cur.right
    #Then leaves
    addLeaves(root, res)
    #Finally right boundary
    cur=root.right
    tmp=[]
    while cur:
        if not isLeaf(cur):
            tmp.append(cur.val)
        if cur.right:
            cur=cur.right
        else:
            cur=cur.left
    while tmp: #Add right boundary in reverse order since you need to go up
        res.append(tmp.pop())
    return res

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5,6,7,None,None,8,9,10,11,12,None])
print(treeBoundary(r))