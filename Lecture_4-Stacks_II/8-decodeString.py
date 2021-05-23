"""
This solution is smart because it prevents the need for pushing each character into stack and reversing the stack to
reconstruct the string.
"""
def decodeString(expr):
    stack=[]
    out=''
    multiplier=0
    for c in expr: #Dont use enumerate if you dont need index k
        if c == '[': #Use elif instead of continue for each if block
            stack.append(out)
            stack.append(multiplier)#Append it now since u have the number already
            #Do this here and not when you see the closing bracket
            multiplier = 0
            out=''
        elif c == ']':
            num=stack.pop()
            prev=stack.pop()
            out = prev + num * out #And thus you prevent reversing the string
        elif c.isdigit(): #better than isnumeric since it is only ascii
            multiplier = multiplier*10 + int(c)
        else:
            out += c

    return out

print(decodeString(list("3[a2[c]]")))