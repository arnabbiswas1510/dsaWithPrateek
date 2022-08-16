def mergeIntervals(intervals):
    intervals.sort(key = lambda x: x[0]) #Remember how comparators are used in Python
    res=[]
    curr = intervals[0]
    for i in range(1,len(intervals)):
        #Next 2 lines are the meat of this program
        if curr[1] >= intervals[i][0]:
            curr = (curr[0], max(curr[1],intervals[i][1]))
        else:
            res.append(curr)
            curr = intervals[i]
    res.append(curr)
    return res

print(mergeIntervals([(8,10),(4,6),(20,21),(1,5),(9,15),(3,4),]))