"""
Intuition is to multiply prefix array with postfix array (see image above)
"""
def arrayProductNoSelf(arr):
    postFix=[]
    product=1
    res=[]
    for num in arr[::-1]: #Iterate in reverse
        postFix.append(product)
        product *= num
    postFix=list(reversed(postFix))
    product=1
    for i in range(len(arr)):
        res.append(product*postFix[i])
        product *= arr[i]
    return res

print(arrayProductNoSelf([1,2,3,4]))