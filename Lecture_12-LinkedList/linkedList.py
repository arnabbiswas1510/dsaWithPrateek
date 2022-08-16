"""
Thngs to note:
1. Push appends tp front of list so as to avoid scan

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Push to beginning of list
    def push(self, data):
        n = Node(data)
        n.next=self.head
        self.head=n

    def print(self):
        temp = self.head
        while(temp):
            if(temp.next):
                print(temp.data, end=",")
            else:
                print(temp.data)
            temp=temp.next

    def length(self):
        cnt=0
        temp = self.head
        while(temp):
            cnt+=1
            temp=temp.next
        return cnt

    def reverseRecursive(self, head): #Returns head
        if not head.next: #return head and not null
            return head
        n = self.reverseRecursive(head.next)
        head.next.next=head #remember this and next line, self ...
        head.next=None #Because you need to point the last node to Null
        return n #What is the difference between return here and the one on line 33?

    def isPallindrome(self, right):
        self.left = self.head #Why this step? Note left doesnt change till right reaches the end
        if right is None:
            return True
        isP = self.isPallindrome(right.next)
        if not isP:
            return False
        isP1 = self.left.data == right.data
        self.left = self.left.next
        return isP1

    def fold(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        reversedHalfList = self.reverseRecursive(slow)

        curr=self.head
        while curr != slow:
            temp=curr.next
            temp2=reversedHalfList.next
            curr.next=reversedHalfList
            reversedHalfList.next=temp
            reversedHalfList=temp2
            curr=curr.next.next

ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.head=ll.reverseRecursive(ll.head)
print(ll.length())