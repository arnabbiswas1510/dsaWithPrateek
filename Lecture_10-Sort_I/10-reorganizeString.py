"""
https://leetcode.com/problems/reorganize-string/

Use a greedy algorithm as follows:
1. Obtain count of chars in String and Heapify the counts
2. Pop and append to result top 2 most frequent chars from heap. You need to pop top 2 and not 1 in the loop since result
cannot have same character repeated
3. Reduce count of both characters and push to heap
4. Return empty string if count of any remaining character in heap is greater than 1 (will happen for aaab). Else append
remaining char (if any) to result and return result

See explanation here:
https://www.youtube.com/watch?v=zaM_GLLvysw

"""

import heapq
from collections import Counter

def reorganizeString(S):
    res, c = [], Counter(S)
    pq = [(-value,key) for key,value in c.items()] #Because heapify function computes a min heap
    heapq.heapify(pq)
    while len(pq) > 1:
        a_c, b_c = heapq.heappop(pq)
        a_n, b_n = heapq.heappop(pq)
        res += [b_c, b_n]
        if a_c+1 < 0:
            heapq.heappush(pq, (a_c +1, b_c))
        if a_n+1 < 0:
            heapq.heappush(pq, (a_n +1, b_n))
    if len(pq) > 0:
        a_c, b_c = heapq.heappop(pq)
        if a_c < -1:
            return ""
        else:
            res += [b_c]
    res = ''.join(res)
    return res

"""
Variation of above program that doesnt need to pop two characters in each loop. Do this by:
1. Push prev count to heap in current iter
2. Note and compare how this changes the logic from above. 
"""

def reorganizeString2(S):
    res, c = [], Counter(S)
    pq = [(-value,key) for key,value in c.items()]
    heapq.heapify(pq)
    p_a, p_b = 0, ''
    while pq: #Note change
        a, b = heapq.heappop(pq)
        res += [b]
        if p_a < 0: #Note change
            heapq.heappush(pq, (p_a, p_b))
        a += 1
        p_a, p_b = a, b
    res = ''.join(res)
    if len(res) != len(S): return "" #Note change
    return res

print(reorganizeString("aaab"))