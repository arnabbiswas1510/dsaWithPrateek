"""
Strictly largest next element is harder to do as a recursive call since you are not finding a predefined element
Hence do it in a while loop by assigning the ans to the higher section of array if you are searching for
strictly next greater. Do vice versa is searching for strictly smaller
"""
def nextStrictlyLarger(arr,lo,hi,n):
    ans: int=-1 #Predefine it here in case not found
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if int(arr[mid]) <= n: #The = ensures that the same element is never returned as answer
            hi = mid-1 #Move to left
        else:
            ans=mid # Since you dont have a predefined element
            lo = mid+1
    return ans

def reverse(arr, i):
    j = len(arr)-1
    while i <= j:
        arr[i], arr[j]=arr[j], arr[i]
        i+=1
        j-=1
    return arr

"""
Hard Leetcode problem, can be broken into 3 steps:

1. Find the fist dip after the peak from the right (i)
2. Swap arr[i] with arr[j] where j is the next larger element to arr[i] on it's right (within the peak)
3. Reverse the subarray to the right of i since its a peak and reverse would be the same as sort ascending 
"""
def nextPermutation(arr):
    i=len(arr)-1
    while i >=0 and arr[i-1] > arr[i]:
            i-=1
    j = nextStrictlyLarger(arr,i,len(arr)-1, int(arr[i-1]))
    arr[i-1], arr[j] = arr[j], arr[i-1]
    return reverse(arr,i)

arr=list("236541")
print(nextPermutation(arr))