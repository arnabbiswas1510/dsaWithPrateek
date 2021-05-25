def rotateBy1(arr,n):
    first=arr[0]
    for i in range(n-1): #Be careful of the direction of iteration for proper rotation. Otherwise the same digit gets repeated. This rotates right
        arr[i]=arr[i+1]
    arr[n-1]=first
    return arr

def rotateByN(arr, N):
    l = len(arr)
    for i in range(N):
        rotateBy1(arr, l)

arr=[1,2,3,4,5]
rotateByN(arr,3)
print(arr)