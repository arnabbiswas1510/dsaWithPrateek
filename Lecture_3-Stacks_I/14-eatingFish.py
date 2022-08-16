"""
Eating fish problem

Below given are two arrays indicating the size of the arrays and the direction in which they are moving.
A bigger fish can eat a smaller fish if they are moving in opposite direction.

Two fishes moving in same direction cannot eat each other because all the fishes are moving at a constant speed.
Print the output of the fishes which survives

Fishes with distinct sizes and with their direction of movement from their current index

-10 -11 8 5 3 -4 -6 -9 -2 -1 7

Output :

10 <-- 11 <-- 9 <-- 3 <-- 1 <-- 7 -->

Explanation of output:

Fishes with size 10 and 11 won't collide hence escapes, 4 eats 3, 5 eats 4 , 6 eats 5 , 8 eats 6 , 9 eats 8,
then 2 and 1 survives because their behind bigger fish 9. Fish 7 survives because from its current position
it will not collide with any other fish , hence the output.
"""

def eatingFish(arr):
    # Iterate over the first left fishes since they never get eaten
    for k,v in enumerate(arr): #While num in arr doesnt work
        if v < 0:
            printFish(v)
        else:
            break
    # Iterate and print all opposite moving fishes starting from right moving ones and print only left moving ones
    right=[]
    left=[]
    while k < len(arr):
        if arr[k] >= 0:
            right.append(arr[k])
        else:
            left.append(abs(arr[k]))
        eatFish(right,left)
        #Print left stack if right is empty
        if not right:
            printReverse(left)
        k+=1
    #Finally print all right fishes
    #printReverse(left)
    printReverse(right)

def printReverse(stack):
    rev=[]
    while stack:
        rev.append(stack.pop())
    #Now print rev stack to print in reverse
    while rev:
        printFish(rev.pop())

def eatFish(right, left):
    #Note that this method starts poppping only once both left and right have values
    #So there may be multiple calls to this method before it does anything
    #And once called it will pop potentially from both stacks till one is empty
    while right and left:
        if right[-1] > left[-1]:
            left.pop()
        elif left[-1] > right[-1]:
            right.pop()

def printFish(num):
    print(str(abs(num))+" --> " if num > 0 else str(abs(num))+" <-- ", end="") #Ternary operator, no ':' needed

eatingFish([-10, -11 , 8 , 5 , 3 , -4 , -6 , -9, -2, -1, 7])