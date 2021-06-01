"""
Find the celebrity
In a party of N people, only one person is known to everyone. Such a person may be present in the party,
if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “.
Find the stranger (celebrity) in the minimum number of questions. We can describe the problem input as an
array of numbers/characters representing persons in the party. We also have a hypothetical function
HaveAcquaintance(A, B) which returns true if A knows B, false otherwise.

Tip: Can be solved in O(n^2) by brute force. But below approach is O(2n) = O(n)
"""

MATRIX = [ [ 0, 0, 1, 0 ],
           [ 0, 0, 1, 0 ],
           [ 0, 0, 0, 0 ],
           [ 0, 0, 1, 0 ] ]

def know(a,b):
    return MATRIX[a][b]

def findCelebrity(n):
    st=[]
    for i in range(n):
        st.append(i)
    #First pop 2 people off stack
    a=st.pop()
    b=st.pop()

    while len(st) > 1: #Get to the last person and keep eliminating people who know someone
        if know(a,b):
            a=st.pop()
        else:
            b=st.pop()

    if len(st) == 0: #This could happen if there are only 2 people and none are celebrities
        return -1

    c=st.pop() #Potential celeb

    if know(c,b):
        c=b
    if know(c,a):
        c=a

    for i in range(n): #Ensure c knows no one and everyone knows c
        if i!=c and (know(c,i) or not(know(i,c))):
            return -1
    return c

print(findCelebrity(4))