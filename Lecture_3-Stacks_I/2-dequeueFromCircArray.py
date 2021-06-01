"""
Implement Dequeue using Circular Array
Another implementation of Dequeue is using doubly linked lists

Applications of dequeue: 1. Undo and Redo 2. Pallindrome checker 3. Imp: Job stealing in multiprocessor thread scheduling

You need circular queue because in a linear queue when you dequeue there might be vacant spots still left in the queue since you have 2 different tail (rear, for enqueing) and head (front for dequeing) pointers

In Circular Queue, formula to enqueue => rear = (rear+1)%n. Hence Formula to check ir queue is full = (rear+1)%n == front

"""

length = 5
front = -1  # Always initialize these to -1
rear = -1  # Always initialize these to -1
arr=[None]*length #You cant assign to an array without first initializing it

class Dequeue: #Remember the globals

    def rearInsert(self, num):
        global length,front,rear #Always 3 conditions:
        if self.isEmpty(): #1. Is Queue empty
            front = rear =0
        elif self.isFull(): #2. Is it full, remember this condition
            print("Queue full..cant enqueue")
            return
        else: #3. Normal, add ..
            rear= (rear+1)%length #Remember this is the only way to increment indexes in circular array implementations
        arr[rear]=num

    def frontDelete(self):
        global length,front,rear
        if self.isEmpty(): #1. Is Queue empty
            print("Queue empty..cant dequeue")
            return
        else:
            ret = arr[front]
            if front == rear: #2. Is there only a single element left. Remember this condition
                front = rear =-1
            else: #3. Normal, delete ..
                front = (front+1)%length
        return ret

    #Remember front is always delete and rear is insert so you add 1 to rear and front with these operations
    #But in below operations its the reverse so you delete 1 from front and real
    def frontInsert(self, num):
        global length, front, rear
        if self.isEmpty():  #Empty condition always the same
            front = rear = 0
        elif self.isFull():  #So is full condition
            print("Queue full..cant enqueue")
            return
        else:  # 3. Normal, add ..
            front = (front + length - 1) % length  # This is the only line different from rearInsert
        arr[front] = num

    def rearDelete(self):
        global length, front, rear
        if self.isEmpty():  # 1. Is Queue empty, always same
            print("Queue empty..cant dequeue")
            return
        else:
            ret = arr[front]
            if front == rear:  # 2. Is there only a single element left, always same
                front = rear = -1
            else:  # 3. Normal, delete ..
                rear = (rear + length - 1) % length #Only different line from frontDelete
        return ret

    def peekFront(self):
        global front,arr
        return arr[front]

    def peekRear(self):
        global rear,arr
        return arr[rear]

    def display(self):
        global length,front,rear
        if front == -1 and rear == -1:
            print("Queue is empty")
        else:
            i=front #Remember to initialze i to front and not 0
            while i != rear:
                print(arr[i], end=", ")
                i=(i+1)%length #And remember the increment style
            print(arr[rear])

    def isFull(self):
        global length, front, rear
        return front == (rear + 1) % length

    def isEmpty(self):
        global front, rear
        return front == -1 and rear == -1

if __name__ == '__main__':
    s=Dequeue()
    # pushing element to top of stack
    s.rearInsert(1)
    s.rearInsert(2)
    s.rearInsert(3)
    s.rearInsert(4)
    s.rearInsert(5)
    s.rearInsert(6)
    s.display()
    s.frontDelete()
    s.frontDelete()
    s.frontDelete()
    s.rearInsert(7)
    s.rearInsert(8)
    s.frontInsert(9)
    s.frontInsert(1)
    s.rearDelete()
    s.frontInsert(1)
    s.display()