def twoSum(arr, k):
    visited = {} #As an aside in Python sets are represented as {} but this representation does not support add method.
    #In order to use add you need to initialize as set()
    for i in range(len(arr)):
        if arr[i] in visited:
            return visited[arr[i]], i #if a number shows up in the dictionary already that means the
        #necesarry pair has been iterated on previously
        else:
            visited[k-arr[i]]=i # we insert the required number to pair with should it exist later in the list of numbers
    return -1

print(twoSum([2,7,11,15], 9))

