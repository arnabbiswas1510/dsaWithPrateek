"""
https://leetcode.com/problems/container-with-most-water/

Easier variant of the trapRainWater problem (https://github.com/arnabbiswas1510/dsaWithPrateek/blob/main/Lecture_4-Stacks_II/4-trapRainWater.py)
"""

def mostWaterNaive(num):
    maxArea=-99**99 #A very large number, use instead of float('-inf')
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            maxArea = max(maxArea, (j-i)*min(num[i], num[j]))
    return maxArea

def mostWater(num):
    i,j=0,len(num)-1
    maxArea=-99**99
    while i<j:
        maxArea = max(maxArea, (j-i)*min(num[i], num[j]))
        if i < j:
            i+=1
        else: #Note that this condition also applies for i==j since you can increment i or decrement j if both are equal
            j-=1
    return maxArea

print(mostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))