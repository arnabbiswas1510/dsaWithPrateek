"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""
def sumNumbers(root):
    res=[] #Note the technique to maintain state using global variables
    def func(root,curr):
        if not root.left and not root.right:
            res.append(curr+str(root.val)) #Add leaf
        if root.left:
            func(root.left,curr+str(root.val))
        if root.right:
            func(root.right,curr+str(root.val))
    func(root,"")
    summ=0
    for i in res:
        summ+=int(i)
    return summ

from treeOperations import Tree
t=Tree()
r=t.insertLevelOrder([4,9,0,5,1,])
print(sumNumbers(r))