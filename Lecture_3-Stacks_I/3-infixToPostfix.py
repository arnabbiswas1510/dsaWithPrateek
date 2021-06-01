"""
InfixtoPostfix
Infix you need to follow extra rules ie precedence and associativity of operators. Postfix and Prefix dont need precedence and associativity rules hence they are cheaper in both memory and time. But they are not human friendly.

Infix (Polish) and Postfix (reverse polish).

Stack enables you to convert Infix to Postfix/Prefix by scanning only once.
"""

length = 0 #Global variables need to be outside the class definition
bound = 4
top = -1  # Why? Because you need to start with 0 in push
arr = []

#Below is old code

class Stack: #Remember the globals

    def resize(self):
        global length,bound,arr
        newArr=[None for i in range(length+bound)]
        for i in range(length):
            newArr[i]=arr[i]
        length+=bound
        return newArr

    def push(self,num):
        global length,top,arr
        if top == length-1: #Use top and not len(arr)
            arr = self.resize()
        top+=1
        arr[top]=num #Remember not to use arr.append
        return arr #Push returns arr and not num?

    def pop(self):
        global top,arr
        num = arr[top]
        top -= 1
        return num

    def peek(self):
        global top,arr
        return arr[top]

    def display(self):
        global arr,top
        if top == -1:
            print("Stack is empty")
        else:
            for i in range(top+1):
                print(arr[i], end=", ")
            print()

    def isempty(self):
        global top
        return top == -1

#End of old code

def reverse(str):
    if len(str) == 0:
        return str
    ch=str[0]
    return reverse(str[1:])+ch

def isOp(ch):
    return not(ch.isalpha() or ch.isdigit())

def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch=='*' or ch == '/':
        return 2
    elif ch == '^':
        return 3
    else:
        return 0

def toPostFix(st):
    s = Stack()
    out=""
    for ch in st: #Pythoniic way rather than i n range(len(str))
        if ch.isdigit() or ch.isalpha():
            out+=ch
        elif ch == '(':
            s.push(ch)
        elif ch == ')':
            while s.peek() != '(': #Couldnt do pop here
                out += s.pop()
            s.pop() #Remove '('
        else:   #Operator found
            if isOp(ch):
                #Pop and print all operators that are of lesser precedence
                while not s.isempty() and ((precedence(ch) <= precedence(s.peek())) \
                                           or (precedence(ch) <= precedence(s.peek()) and ch=='^')): #Note this important combination RtoL associativity for ^ along with precendence rule
                    out += s.pop()
                s.push(ch) #And push the higher precedence operator back into stack
    while not s.isempty():
        out += str(s.pop())
    return out

def toPreFix(str):
    str = list(reverse(str)) #1.First reverse the input
    for i in range(len(str)): #2. Inverse all brackets
        if str[i] == '(':
            str[i] = ')'
            continue        #Tricky, rememember to do this
        if str[i] == ')':
            str[i] = '('
    return reverse(toPostFix(str)) #3. Return the reverse of postfix

print(toPreFix("x+y*z/w+u"))