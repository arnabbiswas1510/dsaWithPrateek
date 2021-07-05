"""
https://leetcode.com/problems/ipo/

The idea is each time we find a project with max profit and within current capital capability.
Algorithm:

Create (capital, profit) pairs and put them into PriorityQueue pqCap. This PriorityQueue sort by capital increasingly.
Keep polling pairs from pqCap until the project out of current capital capability. Put them into
PriorityQueue pqPro which sort by profit decreasingly.
Poll one from pqPro, it's guaranteed to be the project with max profit and within current capital capability. Add the
profit to capital W.
Repeat step 2 and 3 till finish k steps or no suitable project (pqPro.isEmpty()).
Time Complexity: For worst case, each project will be inserted and polled from both PriorityQueues once, so the overall
runtime complexity should be O(NlgN), N is number of projects.
"""

import heapq #Priority Queue
def findMaximizedCapital(k, W, Profits, Capital):
    heap = []
    projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][1] <= W:
            heapq.heappush(heap, -projects[i][0])
            i += 1
        if heap: W -= heapq.heappop(heap)
    return W

print(findMaximizedCapital(3,0, [1, 2, 3], [0, 1, 2]))