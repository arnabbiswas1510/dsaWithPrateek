"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

Start with heap consisting of smallest elements from each of the k lists
left is the least element in this heap (ie the range) and right is largest element
The goal is to find the least range. Hence keep popping from the heap and add the next element from list i to the heap,
where i is the list with the smallest element.
Keep computing the range of the new heap till you reach the end of the ith list.

This problem can also be solved sub-optimally in n*k time without a heap by incrementing the ith list and determining
the new left for each new range at a cost of k. But this operation reduces to log k when we use a heap since it returns
left at cost 0 and cost logk for every new insert. Max can be computed inexpensively by comparing prev max (right) with
new element being inserted to heap.

Explanation:
https://www.youtube.com/watch?v=Fqal25ZgEDo
"""
import heapq

def smallestRange(A):
    pq = [(row[0], i, 0) for i, row in enumerate(A)]
    heapq.heapify(pq)

    ans = -1e9, 1e9
    right = max(row[0] for row in A)
    while pq:
        left, i, j = heapq.heappop(pq)
        if right - left < ans[1] - ans[0]:
            ans = left, right
        if j + 1 == len(A[i]):
            return ans
        v = A[i][j+1]
        right = max(right, v)
        heapq.heappush(pq, (v, i, j+1))

print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))