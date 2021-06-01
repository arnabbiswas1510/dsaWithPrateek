def medianOfSorted(X, Y):
    lenX=len(X)
    lenY=len(Y)
    if lenX > lenY:
        medianOfSorted(Y, X)  #Make sure X is shorter array
    lo,hi=0,lenX
    while lo <= hi:
        #First compute the partitions
        partX = (lo+hi)//2
        partY = (lenX+lenY)//2-partX #See img

        #Then the 4 comparison points adjacent to the partition
        maxLeftX= X[partX - 1] if partX > 0 else float('-inf')
        maxLeftY= Y[partY - 1] if partY > 0 else float('-inf')
        minRightX= X[partX] if partX != lenX else float('inf')
        minRightY= Y[partY] if partX != lenY else float('inf')

        #Next perform the cross comparison
        if maxLeftX <= minRightY and maxLeftY <= minRightX: #Established the correct partition
            if (lenX + lenY)%2 != 0: #Odd median point
                return min(minRightY, minRightY)
            else:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2 #Return average in case of even
        elif maxLeftX > minRightY:
            hi = partX - 1
        else:
            lo = partX + 1

print(medianOfSorted([1,3,7,9],[2,4,6,8,10,11]))


