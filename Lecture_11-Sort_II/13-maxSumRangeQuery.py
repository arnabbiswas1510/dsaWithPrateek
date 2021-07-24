"""
https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation

Let's start with the obvious, if there is only one request = [start, end], which covers k = end - start + 1 elements,
then the maximum sum would be the sum of the largest k numbers from nums. Because only elements in between start and
end will count, we will greedily put the largest numbers to the index between start and end. Since we can choose any
permutation, it means we have the freedom to assign numbers from nums to any index we want.

In general, the greedy strategy still works. We need to put the largest number to the index that has been requested the
most. Because if an index has been requested m times, then it will contribute m * (value we assign to that index) to the
final sum. The number of requests plays the role of weight or importance.

Now it boils down to how to compute the number of requests for each index. Since each request is an interval, we can do
this more efficiently than looping over each requested interval and count. A similar problem is Car Pool. (BTW, I also
encountered that problem during a contest, that time I struggled and used a heap).

We can solve this problem in linear time. Starting from an array t = [0] * (len(nums) + 1), for each request =
[start,end], we let t[start] += 1, indicate that every index after this point will be counted 1 more time because of
this request, and t[end + 1] -= 1, indicate that every index after end will be counted 1 less time because of the end
of this request. Now the prefix sum of this array t is corresponds to the number of requests for each index. We choose
array t has length len(nums) + 1, only because we need to ensure end + 1 is within the range when we put t[end+1] -= 1.
To compute the number of requests for indices, we will only count the first len(nums) prefix sums.

We record every prefix sum(i.e. the number of requests) in a new array (or we can do it inplace at t), then we just
follow the greedy strategy, to sort both t and nums, and take the sum of t[i] * nums[i] for all i, i.e. dot product
between t and nums.

Time Complexity:
Let N1, N2 be the size of nums and requests. Since we loop through all requests, that is O(N2), computing prefix sum of
t and looping through nums are O(N1). Finally sorting takes O(N1 * log(N1)), so it is O(N1 * log(N1) + N2).

Space Complexity:
Only new array is t, it is O(N1).
"""

def maxSumRangeQuery(nums, requests):
    mod = 10**9 + 7
    n = len(nums)
    t = [0]*(n + 1)
    for a, b in requests: #Mark request indexes
        t[a] += 1
        t[b + 1] -= 1 #Note that you subtract -1 from end-1 in order for prefix sum to be valid
    for i in range(1, n): #Generate prefix sum
        t[i] += t[i - 1]

    nums.sort()
    t.pop() #Dont need the last item of prefix sum array
    t.sort()

    return sum(a*b for a, b in zip(nums, t)) % mod #Return product of prefixdum and nums[i]

print(maxSumRangeQuery( [1,2,3,4,5,10],[[0,2],[1,3],[1,1]]))