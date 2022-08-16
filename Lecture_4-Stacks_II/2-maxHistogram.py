"""
https://leetcode.com/problems/largest-rectangle-in-histogram/  #84 #HARD

Approach:

Use a monotonically increasing stack to push all items that are greater than top as you iterate through array
"""

def maxHistogram(arr):
    maxArea=float('-inf')
    area=0
    stack=[]
    i=0
    #This algo illustrates a new technique to conditionally iterate through a list
    while i < len(arr):
        #Doing a not/or combination below removes the necessity for a check in the else section
        if not stack or arr[stack[-1]] < arr[i]: #Remember no while here, only push each element that is greater than
            # top for each iteration
            stack.append(i)
            i+=1 #Note that i only gets incremented here
        else:
            top = stack.pop()
            if stack: #Note that top and peek are 2 separate variables. So there is i, peek and top and each matters
                # in the formula. Top is the point where the area is being calculated
                area = arr[top]*(i-stack[-1]-1) #This formula is tricky (i - peek -1)
            else:
                area = arr[top]*i
            maxArea= max(maxArea, area) #Note maxArea gets computed only here and not indented left scope. Hence area
            # is not being computed for every i - only if arr[i] reduces

    while stack: #Note that i stays fixed here since you reached end of array
        top = stack.pop()
        area = arr[top]*(i-stack[-1]-1) if stack else arr[top]*i
        maxArea= max(maxArea, area)

    return maxArea

print(maxHistogram([2, 1, 5, 6, 2, 3]))