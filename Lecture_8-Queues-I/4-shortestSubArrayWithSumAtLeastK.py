"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Simpler case with only positive numbers in arr

No prefixSum array or queue needed for this solution
Since the numbers are all +ve, the sum will always be increasing and hence no need to remove from right of array

https://www.youtube.com/watch?v=NKoHjWl2m8Y
"""
def sumAtLeastKOnlyPositive(arr, k):
    ans=99**99
    sum=0
    l=0 #You only need pointer to front of queue
    for i in range(len(arr)):
        sum += arr[i]
        while sum >= k: #When sum exceeds k
            ans=min(ans, i-l+1) #Standard formula for window size in order to adjust for 0 indexing
            sum -= arr[l] # keep subtracting elements from front of array from sum
            l+=1 #And increase left pointer
    return ans if ans != 99**99 else 0

print(sumAtLeastKOnlyPositive([2,1,3,4],5))

"""
Generic case

What makes this problem hard is that we have negative values. We use a sliding window to keep track of min sum array
The Sliding window solution finds the subarray we are looking for in a linear time complexity. 

"""
from collections import deque
def sumAtLeastK(arr, k):
    ps = [0]*(len(arr)+1) #Always need len+1 for prefix sum for 0th element
    for i in range(len(arr)):
        ps[i+1] = ps[i]+arr[i] #Correct way to initialize prefix sum array
    dq=deque()
    ans=99**99
    for i in range(len(arr)+1): #Since this time we will iterate over prefixSum arr
        #Remove from left of arr as above
        while dq and ps[i] - ps[dq[0]] >= k: #Same logic as +ve only
            ans = min(ans, i-dq.popleft())
        #The below logic is needed since we have -ve numbers in array
        while dq and ps[i] <=  ps[dq[-1]]: #Meaning arr[i-1] was -ve so pop it since it cant contribute
            dq.pop()
        dq.append(i) #Same as append
    return ans if ans != 99**99 else 0

print(sumAtLeastK([2,-1,2,1],3))