def maxHistogram(arr):
    maxArea=float('-inf')
    area=0
    stack=[]
    i=0
    #This algo illustrates a new technique to conditionally iterate through a list
    while i < len(arr):
        #Doing a not/or combination below removes the necessity for a check in the else section
        if not stack or arr[stack[-1]] < arr[i]: #Remember no while here, only push each element that is greater than top for each iteration
            stack.append(i)
            i+=1 #Note that i only gets incremented here
        else:
            top = stack.pop()
            if stack:
                area = arr[top]*(i-stack[-1]-1) #This formula is tricky (i - peek -1)
            else:
                area = arr[top]*i
            maxArea= max(maxArea, area) #Note maxArea gets computed only here and not indented left scope

    while stack:
        top = stack.pop()
        area = arr[top]*(i-stack[-1]-1) if stack else arr[top]*i
        maxArea= max(maxArea, area)

    return maxArea

print(maxHistogram([2, 1, 5, 6, 2, 3]))