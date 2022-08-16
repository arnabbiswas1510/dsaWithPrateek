"""
Implement a Stack from Array
Stack needs to be resizable and should implement common Stack functions

Important thing is push and pop should be O(1)

"""

length = 0 #Global variables need to be outside the class definition
bound = 4
top = -1  # Why? Because you need to start with 0 in push
arr = []

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

if __name__ == '__main__':
    s=Stack()
    # pushing element to top of stack
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.display();

    # pushing more element when stack is full
    s.push(5);
    s.push(6);
    s.display();

    s.push(7);
    s.push(8);
    s.display();

    # pushing more element so that stack can grow
    s.push(9);
    s.display()