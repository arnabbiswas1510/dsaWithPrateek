"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Similar to 2 sum
"""

import collections
def findPairs(nums, k):
    res = 0
    c = collections.Counter(nums)
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            res += 1
    return res

print(findPairs([1,2,4,4,3,3,0,9,2,3], 3))