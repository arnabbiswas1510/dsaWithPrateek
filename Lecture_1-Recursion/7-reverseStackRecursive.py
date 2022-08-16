def sortStack(stack):
    if len(stack) == 0:
        return
    x=stack.pop()
    sortStack(stack)
    doSort(x, stack)
    return stack

def doSort(x, stack):
    if not stack or x > stack[-1]:
        stack.append(x)
    else:
        y = stack.pop()
        doSort(x, stack)
        stack.append(y)

print(sortStack([1, 3, 8, 2, 5, 4]))