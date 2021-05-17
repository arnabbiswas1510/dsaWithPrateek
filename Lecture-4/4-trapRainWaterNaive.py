"""
Simpler approach with extra space -
Approach: we just need to focus on water over a particular bar.
This boils down to the problem of knowing local maxima on both sides of the bar.
Precompute this local maxima in two extra arrays
"""
#using prefix and postfix arrays for local maximas
def getTrappedWater(heights):
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

print(getTrappedWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))