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
        res.append(n.val)
    return res

#DFS Solution
def rightSideViewDFS(root):
    def dfs(root, depth):
        if not root:
            return
        if depth == len(res):
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