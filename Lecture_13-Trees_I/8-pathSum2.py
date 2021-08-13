"""
https://leetcode.com/problems/path-sum-ii/
"""
def hasPathSum2(root, target, path, result):
    if root:
        path.append(root.val)
        if not (root.left or root.right) and target == root.val:
            result.append(list(path)) #V Imp: Append a copy of path to result. Since the state of path keeps changing
            # in this recursive context. Unless u make a copy (list(path), you would get an empty result
        if root.left:
            hasPathSum2(root.left, target-root.val, path, result)
        if root.right:
            hasPathSum2(root.right, target-root.val, path, result)
        path.pop()

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
result=[]
hasPathSum2(r,22,[],result)
print(result)