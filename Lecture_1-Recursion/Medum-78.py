"""
https://leetcode.com/problems/subsets/

Google the recursion tree for this. Important to visualize that to understand the algo below
"""
powerset=[]
def powerSet(nums, n, entry):
    if n == len(nums):
        powerset.append(entry)
        return
    powerSet(nums,n+1,entry +[nums[n]])
    powerSet(nums,n+1,entry)

powerSet([1,2,3],0,[])
print(powerset)
