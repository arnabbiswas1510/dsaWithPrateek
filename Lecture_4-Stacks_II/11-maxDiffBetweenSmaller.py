def nextSmallerElement(arr):
    st=[]
    st.append(0)
    res=[None]*len(arr)
    """
    Use indices instead in the below lines and return result array instead of printing
    Similar logic to NGE
    """
    for i in range(1,len(arr)):
        while st and arr[i] < arr[st[-1]]:
            res[st.pop()] = arr[i]
        st.append(i)
    while st:
        res[st.pop()] = -1
    return res

def maxDiffBetweenSmaller(arr):
    rightSmaller=nextSmallerElement(arr)
    leftSmaller=nextSmallerElement(arr[::-1]) #Pass in the reverse of Array
    maxDiff =-1
    for i in range(len(arr)):
        diff=abs(rightSmaller[i]-leftSmaller[i])
        maxDiff = max(maxDiff, diff)
    return maxDiff

print(maxDiffBetweenSmaller([4, 5, 2, 25]))