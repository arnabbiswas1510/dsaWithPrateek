"""
Simpler approach with extra space -
Approach: we just need to focus on water over a particular bar.
This boils down to the problem of knowing local maxima on both sides of the bar.
Precompute this local maxima in two extra arrays
"""
#using prefix and postfix arrays for local maximas
def getTrappedWaterNaive(heights):
    if not heights: return 0
    left, right = [],[]
    maxx = float('-inf')
    for height in heights:
        maxx = max(maxx,height)
        left.append(maxx)

    #re-initialize maxx variable for traversing list in reverse dxn
    maxx = float('-inf')
    for i in range(len(heights)-1,-1,-1):
        maxx = max(maxx,heights[i])
        right.append(maxx)

    #reversing for makng the order correct.
    right.reverse()

    #boundary buildings have no water over it, so we can skip those in loop for calculating ans
    result = 0
    for i in range(1,len(heights)-1):
        result+=(min(left[i],right[i])-heights[i])
    return result

print(getTrappedWaterNaive([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

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