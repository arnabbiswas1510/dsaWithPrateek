"""
https://leetcode.com/problems/sliding-window-maximum/


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
