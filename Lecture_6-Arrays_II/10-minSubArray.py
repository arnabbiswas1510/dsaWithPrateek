"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is
no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Approach:
The O(n) solution is to use two pointers: l and r. First we move r until we get a sum >= s, then we move l to the right
until sum < s. In this process, store the minimum length between l and r.

Since each element in nums will be visited by l and r for at most once. This algorithm is of O(n) time.
"""

def minSubArray(arr, k):
    left=0
    sum=0
    res=float('inf')
    for i in range(len(arr)):
        sum += arr[i]
        while sum >= k:
            res=min(res, i-left+1) #First set res, i-(k-1) or i-k+1 is a very standard formula for moving window size and such problems
            sum -= arr[left] # Then update sum
            left +=1 #And increment left
    return res

print(minSubArray([1, 4, 45, 6, 0, 19],51))

