"""
  Approach:
    1)put all the elements into hash map with key as number and
    there will be chance of same number in given input, so value will be list of indexes.
    2)iterate through given array check if map contains ( k-sum of i) and resturn that as result
"""

def twoSum(arr, k):
    visited = {} #As an aside in Python sets are represented as {} but this representation does not support add method.
    #In order to use add you need to initialize as set(). But in this problem you need Map, not Set
    for i in range(len(arr)):
        if arr[i] in visited:
            return visited[arr[i]], i #if a number shows up in the dictionary already that means the
        #necesarry pair has been iterated on previously
        else:
            visited[k-arr[i]]=i # we insert the required number to pair with should it exist later in the list of numbers
    return -1

print(twoSum([2,7,11,15], 9))

