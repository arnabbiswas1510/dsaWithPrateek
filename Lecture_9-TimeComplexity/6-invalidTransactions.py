"""
https://leetcode.com/problems/invalid-transactions/

"""
def invalidTransactions(intervals):
    intervals.sort(key = lambda x: (x[0],x[1])) #Remember how comparators are used in Python
    res=[]
    if intervals[0][2]>1000:
        res.append(intervals[0])
    for i in range(1, len(intervals)):
        if intervals[i][2] > 1000:
            res.append(intervals[i])
        elif intervals[i-1][0] == intervals[i][0] and abs(intervals[i-1][1] - intervals[i][1]) < 60 and intervals[i-1][3] != intervals[i][3]:
            res.append(intervals[i])
            res.append(intervals[i-1])
    return res

#print(invalidTransactions([("alice",50,100,"beijing"),("alice",20,800,"mtv")]))
#print(invalidTransactions([("alice",20,800,"mtv"),("alice",50,1200,"mtv")]))
print(invalidTransactions([("alice",20,300,"mtv"),("alice",30,400,"mtv"),("alice",50,400,"mtv")]))