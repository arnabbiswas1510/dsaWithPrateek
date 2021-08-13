"""
https://leetcode.com/problems/path-sum-iii/

Use objects (like arrays or maps) as method params to avoid using global variables
"""
def hasPathSum2(root, target, curr, sumFreq, result):
    if root:
        curr += root.val
        result[0] += sumFreq[curr-target]
        #Now use the backtracking template = choose-explore-unchoose
        #choose
        sumFreq[curr]+=1
        #explore
        if root.left:
            hasPathSum2(root.left, target, curr, sumFreq, result)
        if root.right:
            hasPathSum2(root.right, target, curr, sumFreq, result)
        #unchoose
        sumFreq[curr]-=1

from treeOperations import Tree
from collections import defaultdict
t=Tree()
r=t.insertLevelOrder([10,5,-3,3,2,None,11,3,-2,None,1])
sumFreq= defaultdict(int) #Using this hack saves you from state changes in recursive calls
result= [0] #Use [0] instead as result in order to avoid state overwrites due to recursion call stack.
hasPathSum2(r,8,0,sumFreq, result)
print(result[0])