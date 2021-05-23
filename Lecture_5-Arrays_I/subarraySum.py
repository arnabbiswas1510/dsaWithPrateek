def subarrySum(arr, k):
    sumMap={0:1} #Remember to initialize sumMap with this for the initial state.
    # 0 is a valid sum that would be used in the lookups
    sumSoFar=0
    res=0
    for num in arr:
        sumSoFar += num
        #Important to do this check before adding to the map to avoid double counting
        if (sumSoFar-k) in sumMap: #sumSoFar-k and not k-sumSoFar. Why?
            res += sumMap[sumSoFar-k]
        if sumSoFar in sumMap:
            sumMap[sumSoFar] += 1
        else:
            sumMap[sumSoFar] = 1
    return res

print(subarrySum([1,2,3],3))
