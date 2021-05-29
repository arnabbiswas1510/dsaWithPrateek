"""
The intuition in this code is to jump ranges in the array and ensure that each range is fully lighted.
We ensure each range is fully lighted by checking that at least one of the lamps is lit for that range,
 by iterating backwards over that range
We continue this process till the array end is reached and return the number of such ranges covered
"""
def minLights(A, power):
    n = len(A)
    ans = 0
    left = 0 #start of range to check
    pos = 0 #Current posn within range
    while (left < n):
        pos = min(left + power, n-1) #Remember the total range is 2*power -1
        flag = False
        #Iterate backwards over the range from pos to left and break if you find at least one lighted bulb
        while pos >= left:
            if A[pos] ==1:
                ans+=1
                flag=True
                break
            pos-=1
        #If range cannot be lighted return -1
        if not flag:
            return -1
        left = pos + power-1 #pos is the index of the lighted bulb. Left is power -1 to it's right.
        # This guarantees that if you reach upto left in next iteration, there will be no dark spots
    return ans

print(minLights([0, 0, 1, 0, 1, 0, 0], 3))

def minTaps(n, A):
    dp = [0] + [n + 2] * n
    for i, x in enumerate(A):
        for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
            dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
    return dp[n] if dp[n] < n + 2 else -1

#print(minTaps(5, [3,4,1,1,0,0]))