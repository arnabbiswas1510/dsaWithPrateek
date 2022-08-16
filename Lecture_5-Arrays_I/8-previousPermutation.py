def strictlySmallerFromRight(arr, n):
    i = len(arr)-1
    while i >= 0 and (int(arr[i]) >= n or int(arr[i]) == int(arr[i-1])): #Note the or condition
        # necessary for input like 3113, where you want the leftmost 1 to be swapped
        i-=1
    return i

"""
Similar to and has a lesser step than the next permutation problem but note the conditions identified below
"""
def previousPermutation(arr):
    i=len(arr)-1
    while i >=1 and arr[i-1] <= arr[i]: #Pay attention to this condition, you need to catch the first rise
        i-=1
    j = strictlySmallerFromRight(arr, int(arr[i-1])) #arr[i-1] since its the index of first riser
    arr[i-1], arr[j] = arr[j], arr[i-1]
    return arr

arr=list("19467")
print(previousPermutation(arr))