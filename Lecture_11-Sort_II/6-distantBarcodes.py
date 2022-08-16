"""
https://leetcode.com/problems/distant-barcodes/

Explanation
Sort bar codes depending on its occurrence.
We put the most frequent on every two positions,(first, third, fifth...)
In this we, we make sure that no two adjacent bar codes are equal.
"""
import  collections
def rearrangeBarcodes(packages):
    i, n = 0, len(packages)
    res = [0] * n
    for k, v in collections.Counter(packages).most_common():
        for _ in range(v):
            res[i] = k
            i += 2
            if i >= n: i = 1 #Key step to reset to 1st element if it goes outside array
    return res

print(rearrangeBarcodes([1,1,2,2,3,3]))
