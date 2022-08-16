"""
Permutations of a String.

Use Backtracking
"""

def permute(a, index):
    if index == len(a):
        print(''.join(a))
        return
    for i in range(index, len(a)): # Note: Go from index here, not 0
        a[index], a[i] = a[i], a[index]
        permute(a, index + 1)
        a[index], a[i] = a[i], a[index]


# Driver program to test the above function
string = "ABC"
permute(list(string), 0)

def permute2(a, out, index):
    if index == len(a):
        print(''.join(out))
        return
    for i in range(index, len(a)): # Note: Go from index here, not 0
        out.append(a[i])
        permute2(a, out, index + 1)
        out.pop()


# Driver program to test the above function
string = "ABC"
permute2(list(string),[], 0)