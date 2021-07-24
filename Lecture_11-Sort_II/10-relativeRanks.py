"""
https://leetcode.com/problems/relative-ranks/

Simple problem, sort and return mapping for first 3 elements
"""
def findRelativeRanks(score):
    g = sorted(score, reverse=True)
    d={}
    m=[]
    print(g)
    for i in range(len(g)):
        if i == 0:
            d[g[i]] = "Gold Medal"
        elif i == 1:
            d[g[i]] = "Silver Medal"
        elif i == 2:
            d[g[i]] = "Bronze Medal"
        else:
            d[g[i]] = str(i+1)
    for i in score:
        m.append(d[i])
    return m

print(findRelativeRanks([10,3,8,9,4]))