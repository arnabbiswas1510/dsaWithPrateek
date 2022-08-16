"""
Reverse a String

Good basic problem illustrating tail recursion
"""

def reverse(str):
    if len(str) == 0:
        return
    temp=str[0]
    reverse(str[1:])
    print(temp, end=" ") #How do you return the reversed String? Remember the reversed string is just what is derived from tail recursion

def reverse2(string):
    if len(string) == 0:
        return string
    ch=string[0]
    return str(reverse2(string[1:])) + ch #Understand here the intricacy of when you return and when not

#reverse(list("Arnab"))

"""
Reverse a sentance

Same algo as string reversal. Just invoke function using str.split() instead of list(str)

"""
print(reverse2("Venky is lazy".split()))