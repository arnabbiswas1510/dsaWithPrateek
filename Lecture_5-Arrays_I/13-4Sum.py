def fourSum(arr):
    N=len(arr)
    arr.sort()
    result=set()
    for i in range(N-1):
        for j in range(i+1,N):
            target = 0-arr[i]-arr[j]
            k=j+1
            l=N-1
            while k < l:
                if arr[k] + arr[l] > target:
                    l-=1
                elif arr[k] + arr[l] < target:
                    k+=1
                else:
                    result.add((arr[i], arr[j], arr[k], arr[l]))
                    k+=1
    return result


print(fourSum([1,0,-1,0,-2,2]))