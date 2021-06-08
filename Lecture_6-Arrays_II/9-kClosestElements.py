"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

"""

"""
The O(logN) logic for this problem would dwell down to finding k elements by finding the starting element.

If the starting element is found, [start, start+k] elements can be returned.

Consider binary search paradigm:

if arr[mid] is farther from target than arr[mid+k] which is k places ahead of mid then we need to pull lo
to mid with 1 offset; otherwise we can pull hi at mid.
at the end we'll end up with a value contained by lo's index which can be the starting index of our solution

This implementation is very similar to the find closest element in sorted array problem solved here:
https://www.geeksforgeeks.org/find-closest-number-array/
"""
def kClosest(arr, x, k):
    lo, hi = 0, len(arr)-k #Note hi here or else arrayindexoutofbounds
    while lo<hi:
        mid = (lo + hi)//2
        if x-arr[mid]>arr[mid+k]-x: #Note this comparison is very similar to find closest element.
            # It is done like this since arr[mid] < x < arr[mid+k]
            lo = mid + 1
        else:
            hi = mid #Again note that high=mid and not mid-1 since mid itself is a result here since we are also factoring in mid+k
    return arr[lo:lo+k]

print(kClosest([1,2,3,4,5],3,4))

