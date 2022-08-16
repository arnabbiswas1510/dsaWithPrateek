"""
https://leetcode.com/problems/majority-element/ #169

Use Boyer-Moore Majority Voting Algorithm. Similar to Find Celebrity problem
"""

def majorityElement(nums):
    if not nums:
        return None
    candidate = findCandidate(nums)
    return isMajority(candidate, nums)

#Remember simple logic below
def findCandidate(nums):
    count=0
    for i in range(len(nums)):
        if count == 0:
            majority = nums[i]
            count=1 #Not count +=1
        elif majority == nums[i]:
            count+=1
        else:
            count-=1
    return majority


def isMajority(candidate, nums):
    count=0
    for i in range(len(nums)):
        if nums[i] == candidate:
            count+=1
    if count > len(nums)//2:
        return candidate
    else:
        return None

print(majorityElement([2,2,1,1,1,1,1,2,2]))