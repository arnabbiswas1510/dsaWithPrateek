"""
Solve this problem by using DFS approach. The Complexity is still O(m*n) since no node is visited twice
as you mark it 0 with each visit
"""

def maxAreaOfIsland(mat):
    m, n = len(mat), len(mat[0])
    def dfs(i,j):
        if 0<=i<m and 0<=j<n and mat[i][j]: #mat[i][j] must be 1 else return 0
            mat[i][j]=0 #mark as visited
            return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1) #perform DFS
        return 0 #If cell is 0 return 0
    areas=[dfs(i,j) for i in range(m)for j in range(n) if mat[i][j]] #Cool for comprehension
    return max(areas) if areas else 0

mat=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(mat))