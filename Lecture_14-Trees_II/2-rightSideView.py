"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""

from collections import deque
#BFS Solution
def rightSideView(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        res.append(n.val) #Appending to res here guarantees the right nodes only are added, per BFS traversal logic
    return res

#DFS Solution
"""
The idea here is that in the recursive calls res[depth] will be assigned multiple times per level and ultimately the 
right side nodes will be returned. You append None to the result just to avoid index errors
"""
def rightSideViewDFS(root):
    def dfs(root, depth):
        if not root:
            return
        if depth == len(res): #You get index error if you dont do this
            res.append(None)
        res[depth] = root.val
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)
    res = []
    dfs(root, 0)
    return res

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,None,5,None,4])
print(rightSideViewDFS(r))