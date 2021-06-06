"""
The intuition in this problem is that the peek is always on the side of the increasing slope. See note for why
The important assumption also is that the 2 ends of the array are -int. Hence the edges start and end with very small nos
"""
def findPeakElement(arr):
    lo, hi = 0 , len(arr)-1
    while lo < hi:
        m = (lo + hi)//2
        if arr[m] < arr[m+1]: #Peak will have to be to the right
            lo = m+1
        else:
            hi = m #why not m-1? Because as per line 9, arr[m+1] can also be the answer and you dont want to miss
            # it. But m will never be the answer so lo can me m+1. All depends on logic, no fixed rule for binary search
    return lo

print(findPeakElement([1,2,1,3,5,6,4]))