"""
Reverse a String

Good basic problem illustrating tail recursion
"""

def reverse(str):
    if len(str) == 0:
        return
    temp=str[0]
    str=str[1:]
    reverse(str)
    print(temp, end=" ") #How do you return the reversed String? Remember the reversed string is just what is derived from tail recursion

def reverse2(str):
    if len(str) == 0:
        return str
    ch=str[0]
    return reverse(str[1:])+ch #Understand here the intricacy of when you return and when not

reverse(list("Arnab"))

"""
Reverse a sentance

Same algo as string reversal. Just invoke function using str.split() instead of list(str)

"""
reverse("Venky is a lazy guy".split())