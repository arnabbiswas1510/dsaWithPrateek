"""
https://leetcode.com/problems/stone-game-vi/

Intuition
Sort stones by their sum value for Alice and Bob.
If a stone is super valued for Alice, Alice wants to take it.
If a stone is super valued for Bob, Alice also wants to take it.
Because she doesn't want Bob to take it.


Explanation
Here is more convinced explanation.
Assume a stone valued [a,b] for Alice and Bod.
Alice takes it, worth a for Alice,
Bob takes it, worth b for Bob,
we can also consider that it worth -b for Alice.
The difference will be a+b.
That's the reason why we need to sort based on a+b.
And Alice and Bob will take one most valued stone each turn.


Complexity
Time O(nlogn)
Space O(n)

"""
def cmp(a, b): #Since cmp does not exist in Python 3
    return (a > b) - (a < b)

def stoneGameVI(A, B):
    A = sorted(zip(A, B), key=sum)
    return cmp(sum(a for a, b in A[::-2]), sum(b for a, b in A[-2::-2]))

print(stoneGameVI([2,4,3],[1,6,7]))