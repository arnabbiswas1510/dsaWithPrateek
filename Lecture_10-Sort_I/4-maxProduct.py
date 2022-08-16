"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Easy. Key thing here is to find the two highest numbers in O(n)
"""
import math

def maxProduct(nums):
    m = n = -math.inf #m is max and n is second highest
    for num in nums:
        if num >= m:
            n = m #Remember to set 2nd highest to prev highest in this case
            m = num
        elif num > n:
            n = num
    return (m - 1) * (n - 1)

print(maxProduct([1,5,4,5]))