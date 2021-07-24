"""
https://leetcode.com/problems/the-k-strongest-values-in-an-array/

Variation of sort where you sort by distance from median
"""

def getStrongest(arr, k):
    return sorted(arr, key=lambda n: (abs(n - arr[(len(arr) - 1) // 2]), n))[-k:]

print(getStrongest( [6,-3,7,2,11], 3))