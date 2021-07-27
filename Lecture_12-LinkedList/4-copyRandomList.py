"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""

class RndNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.rnd = None

"""
Method 1 ( hashing)
O(N) time and O(N) space

Just store the orignal nodes as key in a map with copy nodes as values
then just assign the corresponding next and radom pointers EASILY
"""
def copyRandomList2(head):
    mp={}
    orig=head
    copy=None
    while orig:
        copy=RndNode(orig.data)
        mp[orig]=copy
        orig=orig.next
    orig=head
    while orig:
        copy=mp[orig]
        copy.next=mp[orig.next] if orig.next != None else None
        copy.rnd=mp[orig.rnd] if orig.rnd != None else None
        orig=orig.next
    return mp[head]

"""
Method 2 (Most Optimal)
O(N) time and O(1) space

Create the copy of node 1 and insert it between node 1 & node 2 in the original Linked List, create a copy of 2 and 
insert it between 2 & 3. Continue in this fashion, add the copy of N after the Nth node

Now copy the random link in this fashion :

original->next->random= original->random->next;
This works because original->next is nothing but a copy of the original and Original->random->next is nothing but a 
copy of the random.

Now restore the original and copy linked lists in this fashion in a single loop.

original->next = original->next->next;
     copy->next = copy->next->next;
"""

def copyRandomList(head):
    curr=head
    #INSERTING THE COPY NEXT TO THE ORIGNAL NODE
    while curr:
        tmp=curr.next
        n = RndNode(curr.data)
        curr.next=n
        n.next=tmp
        curr=tmp
    #ASSIGNING RANDOM FOR THE COPY NODES
    curr=head
    while curr:
        if curr.rnd:
            curr.next.rnd = curr.rnd.next
        else:
            curr.next.rnd=None
        curr=curr.next.next
    #RESTORING THE ORIGNAL LINKED LIST AND COPY LIST
    curr=head
    head2=head.next
    while curr:
        oldNext= curr.next.next
        if oldNext:
            curr.next.next=oldNext.next
        else:
            curr.next.next=None
        curr.next=oldNext
        curr=oldNext
    return head2


def printRnd(head):
    while head:
        print(str(head.data)+','+str(head.rnd.data if head.rnd else 'None'))
        head=head.next

n7=RndNode(7)
n13=RndNode(13)
n11=RndNode(11)
n10=RndNode(10)
n1=RndNode(1)

n7.next=n13
n7.rnd=None
n13.next=n11
n13.rnd=n7
n11.next=n10
n11.rnd=n1
n10.next=n1
n10.rnd=n11
n1.next=None
n1.rnd=n7

copy=copyRandomList(n7)
printRnd(copy)





