"""
The intuition is that one section of the array is sorted
And the goal is to identify that section and perform binary
search only within that section
"""
def searchRotated(arr, k):
    lo=0
    hi=len(arr)-1
    while lo <= hi:
        mid=lo+(hi-lo)//2 #Doing it this way prevents integer overflows.
        # Otherwise (lo+hi)//2 is also fine
        if arr[mid] == k:
            return mid
        if arr[lo] <= arr[mid]: #left side is sorted
            if arr[lo] <= k <= arr[mid]:
                hi = mid-1 #search
            else:
                lo = mid+1
        else: #Right side is sorted
            if arr[mid] <= k <= arr[hi]:
                lo = mid+1
            else:
                hi = mid-1
    return -1

print(searchRotated([3,8,9,11,13,0,1,2],2))