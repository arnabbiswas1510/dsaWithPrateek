"""
Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Approach:

Maintain 1) a frequency array, 2)a visited boolean array and 3) The stack for maintaining the ordered output
The tricky thing is that when you encounter an element at top of the stack which is greater than incoming then
it can be removed and  added later e.g stack = bc remaining string abc then a can pop b and then c
"""

def removeDuplicates(st):
    freq=[0]*26
    visited=[False]*26
    for c in st: #Initialize the freq array
        freq[ord(c)-ord('a')]+=1
    stack=[]
    for c in st:
        i=ord(c)-ord('a')
        freq[i]-=1
        if visited[i]: #Continue if duplicate
            continue
        while stack and c < stack[-1] and freq[ord(stack[-1])-ord('a')] !=0: #WHile top of the stack is greater than and occurs later in input string then reorder
            visited[ord(stack.pop())-ord('a')] = False          #THis is the tricky part
        stack.append(c)
        visited[i]=True
    ret=""
    while stack:
        ret+=stack.pop()
    return ret

print(removeDuplicates("bcabc"))