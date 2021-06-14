"""
https://leetcode.com/problems/maximum-subarray-min-product/

Idea:

ans = 0
For each element nums[i] in array nums:
We treat nums[i] as minimum number in subarray which includes nums[i]
ans = max(ans, nums[i] * getSum(left_bound_index, right_bound_index))
left_bound_index: index of the farthest element greater or equal to nums[i] in the left side
right_bound_index: index of the farthest element greater or equal to nums[i] in the right side
How to build left_bound/right_bound array which store index of the farthest element greater or equal to nums[i] in the left side or in the right side?
Use stack st which keeps index of elements less than nums[i] so far
For i in [0..n-1]:
Pop all elements from st which are greater or equal to nums[i]
If st is not empty: left_bound[i] = st[-1] + 1 (because st[-1] is index of the nearest element smaller than nums[i])
else: left_bound[i] = 0 (because there is no element smaller than nums[i] so far)
Add i to st

In other words for [2,3,3,1,2]

Prefix Sum : [0,2,5,8,9,11]
Right: [2,2,2,4,4] #index-1 is being taken here to accomodate the right most element
Left:[0,1,1,0,4]

(prefix[right+1]-prefix[left)
(8-0)*2=16
(8-2)*3=18
(8-2)*3=18
(11-0)*1=11
(11-8)*2=6

youtube.com/watch?v=c0yTVTI3qlk

Related problems:
Min Stock Span: https://github.com/arnabbiswas1510/dsaWithPrateek/blob/main/Lecture_4-Stacks_II/1-stockSpan.py
Max Histogram: https://github.com/arnabbiswas1510/dsaWithPrateek/blob/main/Lecture_4-Stacks_II/2-maxHistogram.py
"""

def maxSumMinProduct(nums):
    n = len(nums)
    left_bound, right_bound = [0] * n, [0] * n
    st = []
    #First compute smallest element on left
    for i in range(0, n):
        while st and nums[st[-1]] >= nums[i]:
            st.pop()
        if len(st) > 0:
            left_bound[i] = st[-1] + 1
        else:
            left_bound[i] = 0
        st.append(i)

    st = []
    #Then smallest on right (-1 for adjustment)
    for i in range(n - 1, -1, -1):
        while st and nums[st[-1]] >= nums[i]:
            st.pop()
        if len(st) > 0:
            right_bound[i] = st[-1]-1
        else:
            right_bound[i] = n - 1
        st.append(i)

    #Then prefix sum
    preSum = [0] * (n + 1)
    for i in range(n):
        preSum[i + 1] = preSum[i] + nums[i]

    def getSum(left, right):  # left, right inclusive
        return preSum[right+1] - preSum[left]

    maxProduct = 0
    #Finally ans = max(ans, nums[i] * getSum(left_bound_index, right_bound_index))
    for i in range(n):
        maxProduct = max(maxProduct, nums[i] * getSum(left_bound[i], right_bound[i]))
    return maxProduct % 1000_000_007 #This is cool, see: https://www.geeksforgeeks.org/modulo-1097-1000000007/

print(maxSumMinProduct([2,3,3,1,2]))