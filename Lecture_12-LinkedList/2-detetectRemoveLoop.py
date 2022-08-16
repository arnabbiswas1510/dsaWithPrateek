from linkedList import LinkedList

"""
Uses Floyd's cycle detection algorithm - Use a slow and fast pointer. If they meet then there is a loop.
You can optimize by making fast pointer even faster (step 3 at a time, for example) 
"""
def detectAndRemoveLoop(head):
    slow_p = fast_p = head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        # If slow_p and fast_p meet at some poin
        # then there is a loop
        if slow_p == fast_p:
            removeLoop2(head, slow_p)

            # Return 1 to indicate that loop if found
            return 1

    # Return 0 to indicate that there is no loop
    return 0


def removeLoop(head, loop_node):
    # Loop node is any node in loop
    # Set a pointer to the beginning of the linked
    # list and move it one by one to find the first
    # node which is part of the linked list
    ptr1 = head
    while(1):
        # Now start a pointer from loop_node and check
        # if it ever reaches ptr2
        ptr2 = loop_node
        while(ptr2.next != loop_node and ptr2.next != ptr1):
            ptr2 = ptr2.next

        # If ptr2 reached ptr1 then there is a loop.
        # So break the loop
        if ptr2.next == ptr1:
            break

        ptr1 = ptr1.next

    # After the end of loop ptr2 is the lsat node of
    # the loop. So make next of ptr2 as NULL
    ptr2.next = None

"""
Optimized version which is not n^2 as above
Approach:
1. Detect loop and get pointer to loop node
2. Count # of nodes in loop (k)
3. Fix one ptr to head and another to k nodes from head
4. Move both pointers at same pace, they will meet at loop start
5. Proceed to last Node in loop and set it's next to None
"""
def removeLoop2(head, loop_node):
    ptr1 = loop_node
    ptr2 = loop_node

    # Count the number of nodes in loop
    k = 1
    while(ptr1.next != ptr2):
        ptr1 = ptr1.next
        k += 1

    # Fix one pointer to head
    ptr1 = head

    # And the other pointer to k nodes after head
    ptr2 = head
    for i in range(k):
        ptr2 = ptr2.next

    # Move both pointers at the same place
    # they will meet at loop starting node
    while(ptr2 != ptr1):
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    # Get pointer to the last node
    while(ptr2.next != ptr1):
        ptr2 = ptr2.next

    # Set the next node of the loop ending node
    # to fix the loop
    ptr2.next = None


# Driver code
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

detectAndRemoveLoop(llist.head)

print("Linked List after removing loop")
llist.print()


