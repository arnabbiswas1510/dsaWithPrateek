"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

Important thing to understand in this problem is that the bottom pile (n/3) is Bob's so you dont iterate there.
Next when you pick alternate coins out of the remaining 2n/3 coins, you are guaranteed to pick only n/3 coins,
which is the number that you must pick. In neither solution below are you explicitly checking that you have
picked only n/3 coins
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