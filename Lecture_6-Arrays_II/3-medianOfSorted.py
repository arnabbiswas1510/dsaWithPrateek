def medianOfSorted(X, Y):
    lenX=len(X)
    lenY=len(Y)
    if lenX > lenY:
        medianOfSorted(Y, X)  #Make sure X is shorter array
        """ This is because if X is the longer array then you will be performing binary search on this array,
        which will be slower than performing it on the shorter array
        """
    lo,hi=0,lenX
    while lo <= hi:
        #First compute the partitions
        partX = (lo+hi)//2 #You are performing binary search on this array since it is shorter
        partY = (lenX+lenY)//2-partX #This is the partition that will be automatically controlled by the logic,
        # you are not explicitly seraching on this one

        #Then the 4 comparison points adjacent to the partition
        maxLeftX= X[partX - 1] if partX > 0 else float('-inf')
        maxLeftY= Y[partY - 1] if partY > 0 else float('-inf')
        minRightX= X[partX] if partX != lenX else float('inf')
        minRightY= Y[partY] if partX != lenY else float('inf')

        #Next perform the cross comparison
        if maxLeftX <= minRightY and maxLeftY <= minRightX: #Establish the correct partition, this is because all
            # elements on left of the partition needs to be greater than all elements on right, for this to be
            # correct partition. And hence this logic
            if (lenX + lenY)%2 != 0: #Odd median point
                return max(minRightY, minRightY) #The left will always have the extra element in case of odd sum
            # and it will obviously need to be the larger of the two in order to be the median
            else:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2 #You are identifying the two numbers
                # which will be adjacent to the median in the combined array. These two numbers are max(l1,l2) and min(r1,r2)
                # Return average of these two numbers as you do for median of even sized array
        elif maxLeftX > minRightY:
            hi = partX - 1 #We need to move the partition towards the left hand side of X in order to make maxLeftX < maxRightY
        else:
            lo = partX + 1 #Else we move partition towards the right side of X

print(medianOfSorted([1,7,9],[2,8,11]))


