def threeSum(arr):
    N=len(arr)
    arr.sort()
    result=set()
    for i in range(N):
        target = 0-arr[i]
        j=i+1
        k=N-1
        while j < k:
            if arr[j] + arr[k] > target:
                k-=1
            elif arr[j] + arr[k] < target:
                j+=1
            else:
                result.add((arr[i], arr[j], arr[k]))
                j+=1
    return result


print(threeSum([-1,0,1,2,-1,-4]))