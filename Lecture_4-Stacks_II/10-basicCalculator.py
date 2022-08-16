"""
Similar to decodeString
Algorithm:
1. Push result (the part within and sign every time you see open paren and set result=0 and sign=1
2. At every +,-and ) perform computation for result and adjust number=0 and sign=1
3. At closing paren also pop last 2 (result and sign) off stack and add to result
"""

def basicCalculator(expr):
    stack=[]
    number=0
    sign=1
    result=0
    for c in expr:
        if c == '(':
            stack.append(result)
            stack.append(sign)
            result = 0 #Set result = 0 only on open paren
            sign= 1
        elif c == ')':
            result += sign * number
            number=0 #Everywhere else set num = 0
            result *= stack.pop()
            result += stack.pop()
        elif c.isdigit():
            number = number*10 + int(c)
        elif c == '+':
            result += number*sign
            number=0
            sign = 1
        elif c == '-':
            result += number*sign
            number=0
            sign = -1 #You need this because sign is not left or right associative

    result+= number*sign
    return result

print(basicCalculator(list("(1+(4+5+2)-3)+(6+8)")))