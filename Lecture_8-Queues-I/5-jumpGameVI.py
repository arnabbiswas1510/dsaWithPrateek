"""
https://leetcode.com/problems/jump-game-vi/

Intuition:
Algo: Dynamic Programming array for max jump for each i in nums
    dp[i]:the max score u get at index i
    dp[0] = nums[0]
    dp[i] = max(nums[i]+dp[i-1],nums[i]+dp[i-2]..nums[i]+dp[i-k])

Use Deque to keep track of max k using sliding window

https://www.youtube.com/watch?v=3LRL-aHkDDI

Related question: (Folows same algo except for the dp)
https://github.com/arnabbiswas1510/dsaWithPrateek/blob/main/Lecture_7-Arrays_III/1-slidingWindowMaximum.py

Check problems related to monotonic stacks and queues here:
http://www.algorithmsandme.com/monotonic-queue/
"""

def maxResult(nums, k):
    from collections import deque
    dp=[0]*len(nums)
    dp[0]=nums[0]
    d=deque([(nums[0],0)]) #Store both value and index in d
    for i in range(1,len(nums)):
        dp[i] = nums[i] + d[0][0] #Compute jump for i with oldest value from d
        while d and d[-1][0] < dp[i]: #Keep popping latest from queue if its smaller than incoming jump
            d.pop()
        d.append((dp[i],i)) #Append incoming jump to queue

        if i-k == d[0][1]: #pop off left of q if window has moved
            d.popleft()

    return dp[-1] #Last jump will be max

print(maxResult([1,-5,-20,4,-1,3,-6,-3],2))
