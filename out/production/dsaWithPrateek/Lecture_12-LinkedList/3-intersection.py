from linkedList import LinkedList
"""
Approach:
1. Get counts of l1 and l2 and diff them
2. Advance the longer list by diff nodes. This ensures that you meet when you advance both lists by 1
3. Advance both lists by 1 and return the node where the data matches
"""
def getNode(diff, c2, c1):
    while diff:
        c2=c2.next
        diff -=1
    while c1 and c2:
        if c1.data == c2.data:
            return c1.data
        c1 = c1.next
        c2 = c2.next
    return -1

def intersectionNode(ll1,ll2):
    c1, c2 = ll1.length(), ll2.length()
    diff = abs(c1-c2)
    if c1>c2:
        return getNode(diff, ll1.head, ll2.head)
    else:
        return getNode(diff, ll2.head, ll1.head)

# Driver code
ll1 = LinkedList()
ll1.push(3)
ll1.push(4)
ll1.push(9)
ll1.push(15)
ll1.push(30)
ll1.push(31)
ll1.push(32)
ll1.head=ll1.reverseRecursive(ll1.head)

ll2 = LinkedList()
ll2.push(10)
ll2.push(16)
ll2.push(30)
ll2.push(31)
ll2.push(32)
ll2.head=ll2.reverseRecursive(ll2.head)

print(intersectionNode(ll1,ll2))