"""
1. Work left to right
2. Examine each item and compare it to items on its left
3. INSERT the item in the correct position in the array

*The array will form sorted and unsorted partitions
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

print(insertionSort([2,8,5,3,9,4]))

