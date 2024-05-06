"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/

This is the Josephus problem
"""

def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n-1,k)+k)%n #TODO: Mind where you put brackets
    #return (josephus(n - 1, k) + k-1) % n + 1; #More convoluted if u use 1 based indexing and return 1 in line 9

print(josephus(6,2))