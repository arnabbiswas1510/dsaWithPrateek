"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Standard algo similar to finding strictly lesser element, Only variation
is that you have to set result when it is == target and not <= target, as indicated below
You could have returned lo-1 and hi+1, but you would miss the scenario where the number
doesnt exist in the array (-1, -1)
"""
def findLastPosition(arr, k):
    lo, hi = 0, len(arr)-1 #starting hi is always len-1
    result=-1
    while (lo <= hi): #Why do we need <= here?
        mid = (lo + hi) // 2
        if arr[mid] <= k:
            lo = mid + 1
        else:
            hi = mid - 1
        # You need this step explicitly when you are returning
        # the first/last index of the number
        if arr[mid] == k:
            result = mid
    return result

def findFirstPosition(arr, k):
    lo, hi = 0, len(arr)-1 #starting hi is always len-1
    result=-1
    while (lo <= hi): #Why do we need <= here?
        mid = (lo + hi) // 2
        if arr[mid] >= k:
            hi = mid - 1
        else:
            lo = mid + 1
        if arr[mid] == k:
            result = mid
    return result

def findFirstAndLastPosition(arr, k):
    return (findFirstPosition(arr, k), findLastPosition(arr, k))

print(findFirstAndLastPosition([5,6,7,7,8,8,8,8,9,10],8))