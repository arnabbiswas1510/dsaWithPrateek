"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
#1673

This is a good problem to apply stack, with the following idea: let us traverse original list number by number and put
in into stack: if it happens that new number is less than the top of our stack and if we still can afford to delete one
more number, we extract it from stack and put new number. Let me illustrate this on example [1,4,5,3,2,8,7] and k = 4.

First, we put 1 into stack, then 4 and then 5, so far we have [1, 4, 5]. Next step we see number 3, which is less then
5, so we keep removing elements from stack until we can and put 3, so we have [1, 3] now. Next number is 2, so we again
remove 3 and put 2, and we have [1, 2] in our stack now. At this moment number of attempts we can make is equal to zero,
so we just must take all the rest numbers, so finally we have [1, 2, 8, 7] in our stack.

Complexity: both time and space complexity is O(n), where n is length of our string, because for each digit it goes in
and goes out of stack only once.
"""

def mostCompetitive(nums, k):
    remainingElements = len(nums) - k #This is important because you dont want to pop from the stack if you dont have
    # enough elements left in input array
    stack = []
    for num in nums:
        while stack and num < stack[-1] and remainingElements > 0:
            stack.pop()
            remainingElements -= 1
        stack.append(num)

    return stack[:k]

print(mostCompetitive([2,4,3,3,5,4,9,6], 4))