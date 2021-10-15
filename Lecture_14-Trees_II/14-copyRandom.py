"""
https://leetcode.ca/2019-12-24-1485-Clone-Binary-Tree-With-Random-Pointer/

Easy
Use a map to record visited nodes
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.random = None

def constructRandom(arr):
    from collections import defaultdict
    m=defaultdict(lambda x : Node(x))
    def construct(arr, i=0):
        n=len(arr)
        root=None
        # Base case for recursion
        if i < n and arr[i][0]:
            root = m[arr[i][0]]
            root.random=m[arr[i][1]]

            # insert left child
            root.left = construct(arr, 2 * i + 1)

            # insert right child
            root.right = construct(arr, 2 * i + 2)
        return root
    return construct(arr)

def copyRandomBfs(root):
    from collections import deque
    if not root:
        return []
    q = deque([root])
    m={}
    m[root]=Node(root.val)
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            nCopy=m.get(n)
            if n.random:
                if n.random in m:
                    m[n.random]=Node(n.random.val)
                nCopy.random=m[n.random]
            if n.left:
                if n.left in m:
                    m[n.left]=Node(n.left.val)
                nCopy.left=m[n.left]
                q.append(n.left) #Append only left and right, not random
            if n.right:
                if n.right in m:
                    m[n.right]=Node(n.right.val)
                nCopy.right=m[n.right]
                q.append(n.right)
    return m[root]

def copyRandomDfs(root): #Preferred method since it is shorter
    m={}
    def copyRandom(root):
        if not root:
            return None
        if root in m:
            return m[root]
        nCopy = Node(root.val)
        m[root] = nCopy

        nCopy.left=copyRandom(root.left)
        nCopy.right=copyRandom(root.right)
        nCopy.random=copyRandom(root.random)
        return nCopy
    return copyRandom(root)

r=constructRandom([[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]])
r= copyRandomDfs(r)
print(r)

"""
PS: function "copyRandomDfs" fails on gfg clone tree problem, though I think its correct implementation.
Another dfs implementation which gets accepted there is as below.
"""

class Solution:
    def cloneTree(self, tree):
        from collections import defaultdict
        mapp = defaultdict()
        def clone(root):
            nonlocal mapp
            if root is None: return
            new = Node(root.data)
            mapp[new] = new
            new.left = clone(root.left)
            new.right = clone(root.right)
            if root.random:
                if root.random in mapp:
                    new.random = mapp[root.random]
                else:
                    new.random = Node(root.random.data)
                    mapp[new.random] = new.random
            else:
                new.random = None
            return new
        return clone(tree)
