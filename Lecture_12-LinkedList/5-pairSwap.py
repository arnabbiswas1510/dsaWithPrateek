"""
https://leetcode.com/problems/swap-nodes-in-pairs/

We require minimum of three pointers. I have used 'temp' for moving forward. 'back' pointer points to the next of
'front' pointer.'front' is the leading pointer which then later connects to 'back'.

This problem is similar to reverse LL in logic

Below is the Iterative Implementation:
"""
from linkedList import LinkedList
def pairSwap(head):
    temp=head
    head=head.next
    while temp and temp.next:
        back=temp
        front=temp.next
        back.next=front.next
        front.next=back
        if temp:
            temp=temp.next
        if temp.next:
            back.next=temp.next
    return head

#Recursive implementation
def pairSwap2(head):
    curr=head
    front=None
    if curr and curr.next:
        front=curr.next
        curr.next=pairSwap2(front.next)
        front.next=curr
    return front if front else curr

ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.head=ll.reverseRecursive(ll.head)
ll.head=pairSwap2(ll.head)
ll.print()
