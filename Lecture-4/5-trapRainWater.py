"""
More sophisticated version of the above approach using 2 pointers
No need for 2 extra arrays hence lesser space
Calculate local maxima and minima for each index using 2 pointers
"""
def trappedWater(num):
    if num == "":
        return 0
    i=0
    j=len(num)-1
    maxLeft=maxRight=0
    totalWater=0
    while i<j:
        maxLeft=max(maxLeft,num[i])
        maxRight=max(maxRight,num[j])
        if maxLeft < maxRight:
            totalWater += maxLeft-num[i]
            i+=1
        else:
            totalWater += maxRight-num[j]
            j-=1
    return totalWater

print("Total water trapped = " + str(trappedWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])))