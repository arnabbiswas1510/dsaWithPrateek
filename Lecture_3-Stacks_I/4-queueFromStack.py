"""
Implement Queue using Stack
Use 2 stacks. Append to Stack 1 to enque. To deque pop all elements from Stack 1 and append to Stack 2 (Make FIFO) and then pop from Stack 2
"""
st1=[]
st2=[]
class QueSt:
    def enque(self, num):
        global st1
        st1.append(num)

    def deque(self):
        global st1, st2
        if not st1 and not st2:
            print("Queue is empty")
            return
        if st2:
            return st2.pop()
        else:
            while st1:
                e = st1.pop()
                st2.append(e)
            return st2.pop()

    def display(self):
        global st1,st2
        st3=st2
        for x in st1:
            st3.append(x)
        print(st3)

que = QueSt()
que.enque(1)
que.enque(2)
que.enque(3)
que.deque()
que.deque()
que.enque(4)
que.deque()
que.display()