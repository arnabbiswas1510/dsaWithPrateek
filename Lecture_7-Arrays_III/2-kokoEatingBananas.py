"""
https://leetcode.com/problems/koko-eating-bananas/

Good related readup on binary search:
https://leetcode.com/problems/koko-eating-bananas/discuss/769702/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.

Very similar to the page allocation problem:
https://www.geeksforgeeks.org/allocate-minimum-number-pages/

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


arr = [30,11,23,4,20]

print("Minimum number of bananas/hr = ",
      findMinimum(arr, 6))