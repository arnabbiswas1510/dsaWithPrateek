"""
https://leetcode.com/problems/deepest-leaves-sum/


"""

class Solution:
    def deepestLeavesSum(self, root) -> int:
        summ = 0
        max_depth = 1
        nodes = []
        def dfs(node, curr_depth):
            if node is None:
                return
            if node.left is None and node.right is None:
                nodes.append((node.val, curr_depth))
                return
            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)

        def bfs(root):
            from collections import deque
            if not root:
                return []
            q = deque([root])
            while q:
                sum=0
                for _ in range(len(q)):
                    n = q.popleft()
                    sum += n.val
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            return sum

        dfs(root, 1)
        max_depth = max([i[1] for i in nodes])
        return sum([i[0] for i in nodes if i[1] == max_depth])

        #return bfs(root)

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([1,2,3,4,5,None,6,7,None,None,None,None,None,None,8])
s=Solution()
print(s.deepestLeavesSum(r))