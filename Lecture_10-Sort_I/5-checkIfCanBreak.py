"""
https://leetcode.com/problems/check-if-a-string-can-break-another-string/

The alphabetical letter order in check function saves us from using sort.

In the check function, the loop is to go through each letter in the alphabetical letter order (a to z) to check if the
following cases will overcome the other cases to make s negative:
1. the letter not in d1 but in d2;
2. or the count of the letter in d1 is smaller than that in d2.
If s is negative at some point in the loop, d2 cannot break d1. Otherwise, d2 can break d1.

Time : O(n).
Space : O(1).
"""
import collections

def check(d1, d2):
    s = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        s += d1[c] - d2[c]
        if s < 0:
            return False
    return True

def checkIfCanBreak(s1: str, s2: str) -> bool:
    d1 = collections.Counter(s1)
    d2 = collections.Counter(s2)
    return check(d1, d2) | check(d2, d1)

print(checkIfCanBreak('leetcodee','interview'))