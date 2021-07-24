"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""
def maxCoins(piles):
    return sum(sorted(piles)[len(piles)//3 :: 2])

#Expanded version:
def maxCoins2(piles):
    piles.sort()
    m = len(piles)-2 #Start from second last element
    b,res = 0, 0
    while b < m: #Note how you loop over the array. Why?
        res += piles[m]
        m-=2
        b+=1
    return res

print(maxCoins([2,4,1,2,7,8]))