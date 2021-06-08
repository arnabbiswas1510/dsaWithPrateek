"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and
will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Clarification of the Examples: You find the smallest number between the min and max piles which will allow koko to
finish all bananas within the allocated hours.

So for Example 1 number of hours taken for all bananas in piles if she eats 4 bananas/hr= [1,2,2,3] whose sum is 8
With 3/hr : [1,2,3,4] whose sum is 10 so too many hours
With 5/hr : [1,2,2,3] so sum is also 8 but too many bananas/hr
"""
from math import ceil

# Returns false if curr_k doesnt complete all bananas in h hours
def isFeasible(arr, h, curr_k):
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += ceil(arr[i]/curr_k)
        if curr_sum > h:
                return False
    return True

# function to find minimum k
def findMinimum(arr, h):

    lo, hi = min(arr), max(arr) #Becasue the rate has to be a number that lies within the bounds of the array
    result = 10**9

    # Below logic returns the smallest mid that is feasible
    while (lo <= hi): #Why do we need <= here?

        # check if mid works
        mid = (lo + hi) // 2
        if (isFeasible(arr, h, mid)):
            result = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return result


arr = [3,6,7,11]

print("Minimum number of bananas/hr = ",
      findMinimum(arr, 8))