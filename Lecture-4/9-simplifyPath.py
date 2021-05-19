"""
Simpler variation of decodeString
"""
def simplifyPath(expr):
    stack=[]
    for folder in expr.split('/'): #Had to take this approach instead to split by folders
        if stack and folder == '..':
            stack.pop()
        elif folder not in ['.', '..', '']: #Remember to add empty string too
            stack.append('/'+folder)
    out=''
    while stack:
        out = stack.pop() + out#append in reverse
    return out

print(simplifyPath("/a/./b/../c/"))