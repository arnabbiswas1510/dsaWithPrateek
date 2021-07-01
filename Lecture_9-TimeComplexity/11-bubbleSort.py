"""
Iterate the entire array repeatedly and swap alternate elements
Every successive iteration the last elements will be sorted. So exlude that in inner loop
You can optimize as shown below to early exit if there was no swap in an entire inner loop
"""
def bubbleSort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]: #Note what you need to swap (not i,j), since you are swapping adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if not swapped:
            return arr
    return arr

def bubbleSort2(arr): #This is the version I had learnt
    for i in range(len(arr)):
        swapped=False
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]: #Note what you need to swap (not i,j), since you are swapping adjacent elements
                arr[i], arr[j] = arr[j], arr[i]
                swapped=True
        if not swapped:
            return arr
    return arr

print(bubbleSort2([3,5,2,4,8,1,9]))