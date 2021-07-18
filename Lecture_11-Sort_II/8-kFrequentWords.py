"""
https://leetcode.com/problems/top-k-frequent-words/

Below approach uses heaps. Very similar to kFrequentElements problem
"""
from collections import Counter
import heapq

def topKFrequent(words, k):
    freq = Counter(words)
    return heapq.nsmallest(k, freq, key=lambda k: [-freq[k], k])

"""
Alternate approach using sorted
Similar to: 
"""

def topKFrequent2(words, k):
    ht = Counter(words)
    return sorted(ht, key = lambda x: (-ht[x], x))[:k]

print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))