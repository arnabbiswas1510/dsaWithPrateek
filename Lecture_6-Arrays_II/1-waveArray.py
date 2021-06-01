"""
Simple if you know the approach. Approach is to maintain a an increasing flag or i-1 and i and swap
i+1 and i if increasing if True and i < i+1
"""

def waveArray(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            increasing=True
        else:
            increasing=False
        if increasing and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(waveArray([1,2,9,4,8]))