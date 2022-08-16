"""
https://leetcode.com/problems/sort-colors/

An easier variation of this problem is to sort a binary array. This can be easily solved by running two pointers
from either end and swapping 1s on left with 0s on right

Array, 2 pointer, Sorting
"""
def dutchFlag(arr):
    lo = mid = 0
    hi=len(arr)-1
    while mid <= hi: #We shouldnt do lo here since lo will always be behind mid
        if arr[mid] == 0: #always check arr[mid] in each if with the 3 conditions
            arr[mid], arr[lo] = arr[lo], arr[mid] #swap with lo since lo tracks 0
            mid+=1 #Must increment mid here since mid is with lo and has already been verified
            lo += 1
        elif arr[mid] == 1:
            mid += 1 #No swapping needed since mid tracks 1
        else:
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi-=1 #TODO Why dont we increase mid here??
    return arr

print(dutchFlag([2,2,1,0,1,1,2,0,0]))