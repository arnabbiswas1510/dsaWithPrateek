"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


Approach:

Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing, and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.

For each index i:

1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
4. If our window has reached size k, append the current window maximum to the output.
"""
import collections

def slidingWindowMax(nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n: #remove all elements in d that are less than incoming
            d.pop()
        d += i, #Add index of incoming to d
        if d[0] == i - k: #pop leftmost element if it is falling out of window
            d.popleft()
        if i >= k - 1: #Once i exceeds window size keep adding max for window to out. This will be the first index in d
            out += nums[d[0]],
    return out

print(slidingWindowMax([1,3,-1,-3,5,3,6,7], 3))
