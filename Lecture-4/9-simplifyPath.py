"""
Simpler variation of decodeString
"""
def simplifyPath(expr):
    stack=[]
    for folders in expr.split('/'): #Had to take this approach instead to split by folders
        if stack and folders == '..':
            stack.pop()
        elif folders not in ['.', '..', '']: #Remember to add empty string too
            stack.append(folders)
    out=''
    while stack:
        out += '/'+stack.pop() #append in reverse
    return out

print(simplifyPath("/a/./b/../../c/"))