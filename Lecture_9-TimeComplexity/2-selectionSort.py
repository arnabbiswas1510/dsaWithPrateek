"""
During each iteration, select the smallest item from the unsorted partition and move it to the sorted partition
"""
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selectionSort([2,8,5,3,9,4,1]))