"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
"""
from treeOperations import Node

#Expected answer is [0,-3,9,-10,null,5], but below prints [0,-10,5,null,-3,null,9]
def sortedArrayToBSTNotWorking(nums, start,end):
    if start<=end:#If you do < and not <= you  will miss out numbers from the tree
        mid= start+(end-start)//2 #No difference between this and the whole thing within int() instead
        n=Node(nums[mid])
        n.left=sortedArrayToBST(nums, start, mid-1)
        n.right=sortedArrayToBST(nums, mid+1, end)
        return n


def sortedArrayToBST(nums):
    if len(nums)==0: #Note the return condition here
        return None
    mid= len(nums)//2 #Just len/2, no start and end needed
    n=Node(nums[mid])
    n.left=sortedArrayToBST(nums[:mid])
    n.right=sortedArrayToBST(nums[mid+1:])
    return n


from treeOperations import Tree
t=Tree()
nums=[-10,-3,0,5,9]
r=sortedArrayToBST(nums) #Remember the 'len- 1' if you are passing start and end
t.printLevelOrder(r)