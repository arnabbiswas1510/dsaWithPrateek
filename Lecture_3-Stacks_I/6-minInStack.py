"""
Minimum element in Stack
Trivial approach is to maintain another min stack and keep pushing to the stack every incoming element that
is smaller than the top of the stack. Then when popping from first stack if min element is being popped then pop
off the min stack. This apprach requires O(n) extra space and O(1) time. Design an algorithm with O(1) time AND space
"""
class minStack:
    def __init__(self):
        self.st=[]
        self.min=None

    def push(self, num):
        if not self.min:
            self.min=num
            self.st.append(num)
        elif num < self.min: #If incoming number is less than min,
            x = 2*num - self.min
            self.min=num #set min as incoming
            self.st.append(x) #and push 2*incoming - prev min to stack
        else:
            self.st.append(num)

    def pop(self):
        if not self.st:
            print("Stack is empty")
            return
        x = self.st.pop()
        if x < self.min: #If top of stack is less than min
            self.min = 2 * self.min - x #Set min to this
            return self.min #And return min as popped value
        else:
            return x

    def display(self):
        print(self.st)

    def getMin(self):
        return self.min


stack = minStack()

stack.push(3)
stack.push(5)
print(stack.getMin())
stack.push(2)
stack.push(1)
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()