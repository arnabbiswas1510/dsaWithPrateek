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

def maxRectangle(rect):
    area=0
    maxArea=float('-inf')
    for i in range(len(rect)):
        row = [0]*len(rect[i])
        for j in range(len(rect[i])):
            if rect[i][j]==0:
                row[j]=0
            else:
                for k in range(i+1):
                    row[j] += rect[k][j]
        area=maxHistogram(row)
        maxArea = max(maxArea, area)
    return maxArea

rect=[[1,0,1,0,0],
      [1,0,1,1,1],
      [1,1,1,1,1],
      [1,0,0,1,0]]

print(maxRectangle(rect))