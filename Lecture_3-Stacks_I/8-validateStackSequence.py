"""
Validate Stack Sequence
Problem Statement :

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the
result of a sequence of push and pop operations on an initially empty stack.

Sample 1 :

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1] Output: true Explanation: We might do the following sequence:

push(1), push(2), push(3), push(4), pop() -> 4, push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Sample 2 :

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2] Output: false

Explanation: 1 cannot be popped before 2.

Solution: https://www.youtube.com/watch?v=vHKXT0cSI54
"""

def validate(pushed, popped):
    st=[]
    i =0
    for num in pushed:
        st.append(num)
        while st and popped[i] == st[-1]: #Keep popping what u push till its the same as whats in popped array
            st.pop()
            i+=1
    return i == len(popped) #Return true if popped array is fully covered


print(validate([1,2,3,4,5],[4,5,3,2,1]))