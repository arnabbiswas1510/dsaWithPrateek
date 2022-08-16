"""
https://medium.com/@rushyab/aggressive-cows-spoj-75a155bfe749

Identical to koko eating bananas problem

Write function that returns bool indicating if cows can be placed at distance k
Then binary search for the largest k

https://www.youtube.com/watch?v=wSOfYesTBRk
"""

from math import ceil

# Returns false if curr_k doesnt fit all cows
def canPlaceCows(arr, h, curr_k):
    cowPosn = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if cowPosn + curr_k <= arr[i]:
            cowPosn = arr[i]
            cnt += 1
        if cnt == h:
            return True
    return False

# function to find minimum k
def findMaxDistance(arr, h):

    lo, hi = min(arr), max(arr)
    result = -99**99

    # Below logic returns the greatest mid that is feasible
    while (lo <= hi): #Why do we need <= here?

        # check if mid works
        mid = (lo + hi) // 2
        if (canPlaceCows(arr, h, mid)):
            result = mid
            lo = mid + 1 #Here this is reverse of koko since you want to try higher in this problem
        else:
            hi = mid - 1

    return result


arr = [1,2,4,8,9]

print("Max distance between cows = ",
      findMaxDistance(arr, 3))