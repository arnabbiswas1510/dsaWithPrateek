"""
https://leetcode.com/problems/top-k-frequent-elements/

Below solution doesnt use heaps
This problem can also be solved in two alternative methods:
1. Using heap: https://youtu.be/RAbhvzPF1Ko
2. Using quickSelect
"""
import collections
def topKFrequent(nums, k):
    h = collections.Counter(nums)
    return [n for (c, n) in sorted([(c, n) for (n, c) in list(h.items())], reverse=True)[:k]]