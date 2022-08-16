"""
https://leetcode.com/problems/all-paths-from-source-to-target

<a href="file:resources/Medium-797.png">/resources/Medium-797.png</a>
"""
class Solution:
    def allPathsSourceTarget(self, graph):
        res=[]
        end=len(graph)-1
        path=[0]
        def dfs(node):
            if node==end:
                res.append(path.copy())
                return
            for next in graph[node]:
                path.append(next)
                dfs(next)
                path.pop()
        dfs(0)
        return res

s=Solution()
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))