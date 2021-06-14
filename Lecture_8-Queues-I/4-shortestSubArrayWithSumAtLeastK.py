
"""
Simpler case is only positive numbers in arr

No prefixSum array or queue needed for this solution
Since the numbers are all +ve, the sum will always be increasing and hence no need to remove from right of array
"""
def sumAtLeastKOnlyPositive(arr, k):
    ans=99**99
    sum=0
    l=0 #You only need pointer to front of queue
    for i in range(len(arr)):
        sum += arr[i]
        while sum >= k: #When you hit a sum at least k keep removing elements from front of array
            ans=min(ans, i-l+1) #Standard formula for window size in order to adjust for 0 indexing
            sum -= arr[l]
            l+=1
    return ans if ans != 99**99 else 0

print(sumAtLeastKOnlyPositive([2,1,3,4],5))

"""
Generic case

What makes this problem hard is that we have negative values. If you haven't already done the problem with positive 
integers only, I highly recommend solving it first, as I will use its Sliding Window solution to reach the Deque 
solution here. You can find the problem here , and a Sliding window solution here.

Recall of the Sliding window solution in a positive array
The Sliding window solution finds the subarray we are looking for in a linear time complexity. The idea behind it is 
to maintain two pointers: start and end, moving them in a smart way to avoid examining all possible values 0<=end<=n-1 
and 0<=start<=end (to avoid brute force).

What it does is:

Incremeting the end pointer while the sum of current subarray (defined by current values of start and end) is smaller 
than the target.
Once we satisfy our condition (the sum of current subarray >= target) we keep incrementing the start pointer until we 
violate it (until sum(array[start:end+1]) < target).
Once we violate the condition we keep incrementing the end pointer until the condition is satisfied again and so on.
The reason why we stop incrementing start when we violate the condition is that we are sure we will not satisfy it 
again if we keep incrementing start. In other words, if the sum of the current subarray start -> end is smaller than 
the target then the sum of start+1 -> end is neccessarily smaller than the target. (positive values)
The problem with this solution is that it doesn't work if we have negative values, this is because of the sentence 
above Once we "violate" the condition we stop incrementing start.

Problem of the Sliding window with negative values
Now, let's take an example with negative values nums = [3, -2, 5] and target=4. Initially start=0, we keep moving the end pointer until we satisfy the condition, here we will have start=0 and end=2. Now we are going to move the start pointer start=1. The sum of the current subarray is -2+5=3 < 4 so we violate the condition. However if we just move the start pointer another time start=2 we will find 5 >= 4 and we are satisfying the condition. And this is not what the Sliding window assumes.

Deque solution
The Deque solution is just a modification of the Sliding window solution above. We will modify the way we are updating start.
Let's explain the Deque solution based on the code of @Lee215 by answering some questions :

What does the Deque store :
The deque stores the possible values of the start pointer. Unlike the sliding window, values of the start variable 
will not necessarily be contiguous.

Why is it increasing :
So that when we move the start pointer and we violate the condition, we are sure we will violate it if we keep taking 
the other values from the Deque. In other words, if the sum of the subarray from start=first value in the deque to end 
is smaller than target, then the sum of the subarray from start=second value in the deque to end is necessarily smaller 
than target.
So because the Deque is increasing (B[d[0]] <= B[d[1]]), we have B[i] - B[d[0]] >= B[i] - B[d[1]], which means the sum 
of the subarray starting from d[0] is greater than the sum of the sub array starting from d[1].

Why do we have a prefix array and not just the initial array like in sliding window :
Because in the sliding window when we move start (typically when we increment it) we can just substract nums[start-1] 
from the current sum and we get the sum of the new subarray. Here the value of the start is jumping and one way to 
compute the sum of the current subarray in a constant time is to have the prefix array.

Why using Deque and not simply an array :
We can use an array, however we will find ourselves doing only three operations:
1- remove_front : when we satisfy our condition and we want to move the start pointer
2- append_back : for any index that may be a future start pointer
3- remove_back : When we are no longer satisfying the increasing order of the array
Deque enables doing these 3 operations in a constant time.
"""
from collections import deque
def sumAtLeastK(arr, k):
    ps = [0]*(len(arr)+1) #Always need len+1 for refix sum for 0th element
    for i in range(len(arr)):
        ps[i+1] = ps[i]+arr[i] #Correct way to initialize prefix sum array
    dq=deque()
    ans=99**99
    for i in range(len(arr)+1): #Since this time we will iterate over prefixSum arr
        #Remove from left of arr as above
        while dq and ps[i] - ps[dq[0]] >= k: #Same logic as above
            ans = min(ans, i-dq.popleft())
        #The below logic is needed since we have -ve numbers in array
        while dq and ps[i] - ps[dq[-1]] <= 0:
            dq.pop()
        dq.append(i) #Same as append
    return ans if ans != 99**99 else 0

print(sumAtLeastK([2,-1,2,1],3))