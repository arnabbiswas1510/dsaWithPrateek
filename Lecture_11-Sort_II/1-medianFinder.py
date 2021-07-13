"""
https://leetcode.com/problems/find-median-from-data-stream/

Important problem since for a stream this can be done in logn time. In a fully materialized array the cheapest is nlogn

The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of
smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on
n's parity.

This way we only need to peek the two heaps' top number to calculate median.

Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):

(1) length of (small, large) == (k, k)
(2) length of (small, large) == (k, k + 1)
After adding the number, total (n + 1) numbers, they will become:

(1) length of (small, large) == (k, k + 1)
(2) length of (small, large) == (k + 1, k + 1)
Here we take the first scenario for example, we know the large will gain one more item and small will remain the same
size, but we cannot just push the item into large. What we should do is we push the new number into small and pop the
maximum item from small then push it into large (all the pop and push here are heappop and heappush). By doing this
kind of operations for the two scenarios we can keep our invariant.

Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided us a function "heappushpop"
which saves some time by combine two into one. The document says:

Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently
than heappush() followed by a separate call to heappop().
Alltogether, the add operation is O(logn), The findMedian operation is O(1).

Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".

A further observation is that the two scenarios take turns when adding numbers, thus it is possible to combine the two
into one.
"""

from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num)) #Note in Python the small heap would store -ve vals

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


mf = MedianFinder()
mf.addNum(3)
mf.addNum(2)
mf.addNum(5)
mf.addNum(9)
mf.addNum(4)
mf.addNum(1)
mf.addNum(-1)
mf.addNum(-4)
mf.addNum(-5)
print(mf.findMedian())