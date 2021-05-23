def span(arr):
    span=[None]*len(arr)
    span[0]=1 #Least span is always 1
    stack=[]
    stack.append(0)
    for i in range(1,len(arr)):
        while stack and arr[stack[-1]] < arr[i]: #First pop everything thats smaller than i
            stack.pop()
        span[i] = i - stack[-1] if stack else i+1 #If stack is empty then span is entire array till i, Ternary operations in Python
        #If non empty then above formula is intuitive
        #Note that you are pushing index of i into stack and not the element itself. Because u need to use the index
        stack.append(i)
    return span

print(span([11, 9, 7, 5, 4, 6, 8, 10, 7, 9]))