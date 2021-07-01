"""
https://leetcode.com/problems/insert-interval/

Cool variant of https://github.com/arnabbiswas1510/dsaWithPrateek/blob/main/Lecture_5-Arrays_I/5-mergeIntervals.py

Iterate through the input array as below and create left and right lists and derive s and e when the condition matches
Note that the new s and e will influence future computations of left and right, which is quite cool. This trick makes it
work for all varieties of inputs
"""

def insert(intervals, newInterval):
    s, e = newInterval[0], newInterval[1]
    left, right = [], []
    for i in intervals:
        if i[1] < s:
            left += i, #Note the way we append to the array, but we need the comma else the list will be flat.
            # Keep in mind that this is list concatenation, not adding elements to list
        elif i[0] > e:
            right += i,
        else:
            s = min(s, i[0])
            e = max(e, i[1])
    return left + [[s, e]] + right #Note the addition of mid within double sq brackets

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))