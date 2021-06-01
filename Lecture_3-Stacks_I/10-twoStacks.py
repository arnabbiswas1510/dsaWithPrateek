"""
Two Stacks
Implement two stacks in an array.
"""

class twoStacks:
    def __init__(self, capacity):
        self.arr=[None]*capacity
        self.top1= -1
        self.top2 = capacity #Initialize top2 to capacity instead of -1 to avoid extra code

    def push1(self, val): #Have 2 push methods instead of 1 with a st parameter for more readability
        if self.top1+1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = val
        else:
            print("Stack overflow")

    def push2(self, val):
        if self.top2-1 > self.top1:
            self.top2 -= 1
            self.arr[self.top2] = val
        else:
            print("Stack overflow")

    def pop1(self):
        if self.top1 > -1:
            ret = self.arr[self.top1]
            self.top1 -= 1
            return ret
        else:
            print("Stack underflow")

    def pop2(self):
        if self.top2 < len(self.arr):
            ret = self.arr[self.top2]
            self.top2 += 1
            return ret
        else:
            print("Stack underflow")

    def display(self):
        print(self.arr)

st=twoStacks(10)
st.push1(1)
st.push1(2)
st.push1(3)
st.pop1()
st.push2(4)
st.push2(5)
st.pop2()
st.display()