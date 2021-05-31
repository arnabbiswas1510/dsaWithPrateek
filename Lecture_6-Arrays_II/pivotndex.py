"""
Intuition here is to compute postFix array and then maintain a running prefixSum and return the index at which the two are equal
Remember to stagger both prefix and postfix sums by 1 index in order to exclude the current element as asked in the problem
We do not need to reverse the postFix array here. This is O(n) time and O(n) space. Can be solved in O(1) space as shown in next problem
"""
def pivotIndex(arr):
    postFix=[None]*len(arr)
    postFix[(len(arr)-1)]=0 #Stagger by one index sicne we need to exlude self in the pivot 
    for i in range(len(arr)-2,-1,-1):
        postFix[i]=arr[i+1]+postFix[i+1]
    prefix=0
    #We dont need to reverse the postFix array given the nature of ths problem!!!
    if postFix[0] == prefix:
        return 0
    for i in range(1,len(arr)):
        prefix += arr[i-1]
        if prefix == postFix[i]:
            return i
    return -1

"""
Note below method doesnt work since two varables are needed
"""
def pivotIndexNoSpaceDoesntWork(arr):
    sumArr=sum(arr)
    sumSoFar=0
    for k,v in enumerate(arr):
        if sumSoFar == sumArr - sumSoFar:
            return k #Do this frst since we need to exclude the current index
        else:
            sumSoFar += v
    return -1


def pivotIndexNoSpace(arr):
    right=sum(arr)
    left=0
    for k,v in enumerate(arr):
        right -= v
        if right == left:
            return k #Do this frst since we need to exclude the current index
        else:
            left += v
    return -1



print(pivotIndexNoSpace([1, 7, 3, 6, 5, 6]))
        