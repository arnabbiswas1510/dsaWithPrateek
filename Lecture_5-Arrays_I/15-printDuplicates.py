"""
The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. 
We do this by making elements at arr[i] negative.
"""

def printDuplicates(arr):
    ans=[]
    for num in arr:
        if arr[abs(num)-1] < 0: #Remember abs since this program is making the numbers -ve. Input is all +ve
            ans.append(abs(num)) #Note that you return num here and not arr[num]
        else:
            arr[abs(num)-1] *= -1
    return ans

print(printDuplicates([4,3,2,7,8,2,3,1]))