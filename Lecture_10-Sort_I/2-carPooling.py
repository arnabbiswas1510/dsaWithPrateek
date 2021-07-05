"""
https://leetcode.com/problems/car-pooling/



Similar to: https://leetcode.com/problems/meeting-rooms-ii/discuss/278270/Java-Sort-All-Time-Point
"""
from collections import defaultdict
def carPooling(arr, capacity):
    out = defaultdict(int)
    for trip in arr:
        out[trip[1]] += trip[0]
        out[trip[2]] -= trip[0]
    for i in sorted(out.keys()):
        capacity -= out[i]
        if capacity < 0:
            return False
    return capacity >= 0

print(carPooling([[2,1,5],[3,3,7]], 4))