def deleteConsecutive(strs):
    i=0
    stack=[]
    while i < len(strs):
        if stack and stack[-1] == strs[i]:
            stack.pop()
        else:
            stack.append(strs[i])
        i+=1
    return len(stack)

print(deleteConsecutive("tom jerry jerry tom".split()))
