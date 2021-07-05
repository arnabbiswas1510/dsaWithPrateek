"""
https://leetcode.com/problems/car-pooling/

Solution:
Process all trips, adding passenger count to the start location, and removing it from the end location.
After processing all trips, a positive value for the specific location tells that we are getting more passengers;
negative - more empty seats.

Finally, scan all stops and check if we ever exceed our vehicle capacity.

Similar to: https://leetcode.com/problems/meeting-rooms-ii/discuss/278270/Java-Sort-All-Time-Point
"""
from collections import defaultdict
def carPooling(arr, capacity):
    out = defaultdict(int)
    #Initialize a dictionary of start and end location by key and add passengers (start loc)
    # and remove passengers (end loc) by val
    for trip in arr:
        out[trip[1]] += trip[0]
        out[trip[2]] -= trip[0]
    for i in sorted(out.keys()): #Will not work without the sorted
        capacity -= out[i]
        if capacity < 0:
            return False
    return capacity >= 0

print(carPooling([[2,1,5],[3,3,7]], 4))