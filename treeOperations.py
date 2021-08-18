class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None

class Tree:
    def __init__(self):
        self.starNode=None

#------------------------------Insert Node ------------------------------------

#Note that you cannot pass a null root to this method since you need a handle
    # to insert new node
    def recInsert(self, root, val):
        if root.val < val:
            if root.right:
                self.recInsert(root.right, val)
            else:
                root.right = Node(val)
        else:
            if root.left:
                self.recInsert(root.left, val)
            else:
                root.left = Node(val)

    def insert(self, val):
        self.insert(self.starNode, val)

    """
    For iterative version keep two pointers parent and child
    At the beginning of loop set parent to child. Loop True.
    Advance child left or right depending on val
    if child is null after advancement set parent's L or R to new Node and return
    """
    def insert(self, root, val):
        n = Node(val)
        if not root:
            self.starNode=n
            return n
        parent=None
        child=root
        while True:
            parent=child
            if n.val < child.val: #Move left
                child = child.left
                if not child:
                    parent.left=n
                    return root
            else:
                child = child.right
                if not child:
                    parent.right=n
                    return

#-----------------------------------Find Node ---------------------------------
    def findIter(self, val):
        if self.starNode == None:
            return False

        current = self.starNode
        parent = self.starNode
        isLeftChild = True

        while current.val != val:
            parent = current
            if val < current.val:
                isLeftChild=True
                current=current.left
            else:
                isLeftChild=False
                current=current.right
            if current == None: #Remember this step
                return None, None, None
        return current, parent, isLeftChild

#--------------------------------------Delete Node ----------------------------
    """
    Memory aid: Remember the variables required:
    current (Node to be deleted)
    parent
    isLeftChild (Flag indicating if current is Left child of parent)
    successor (if current has both children)
    """
    def deleteNode(self,val):
        if self.starNode == None:
            return False

        current, parent, isLeftChild = self.findIter(val)

        if current: #Node found
            if not current.left and not current.right: #Case 1: Current is leaf, set parent's L or R to None
                if current == self.starNode:
                    self.starNode = None
                else:
                    if isLeftChild:
                        parent.left = None
                    else:
                        parent.right = None
            elif not current.left: #Case 2: Current has only one child, set parent's L or R to that child
                if current == self.starNode:
                    self.starNode = None
                else:
                    if isLeftChild:
                        parent.left = current.right
                    else:
                        parent.right = current.right
            elif not current.right: #Case 2: Current has only one child, set parent's L or R to that child
                if current == self.starNode:
                    self.starNode = None
                else:
                    if isLeftChild:
                        parent.left = current.left
                    else:
                        parent.right = current.left
            else: #Case 3: Current has both children, most interesting case
                #Get successor - go right once and leftmost
                successor=current.right
                while successor.left:
                    successor=successor.left

                current.val = successor.val
                if not parent:
                    current.right=successor.right
                else:
                    parent.left=successor.right
        return True
#---------------------------------------Adhoc procedures ----------------------------

    """
    Necessary for some versions of delete
    You check for grandchild's existence till leaf but return the child (parent of successor)
    """
    def getSuccessorParent(self, node):
        temp=node.right

        while temp.left.left:
            temp=temp.left

        return temp

#---------------------------------------Tree Traversals -----------------------
    """
    Showing only one recursive implementation since they are most trivial
    """
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=",")
            self.inorder(node.right)

    def inorderIter(self, node):
        st=[]
        while True:
            if node:
                st.append(node)
                node=node.left
            else:
                if st:
                    node=st.pop()
                    print(node.val, end=",")
                    node=node.right
                else:
                    break

    def preorderIter(self, node):
        st=[]
        if node:
            st.append(node)
        while st:
            node=st.pop()
            print(node.val, end=",")
            if node.right: #Since its stack you append in reverse order of printing
                st.append(node.right)
            if node.left:
                st.append(node.left)

    def postorderIter(self, node): #Trickiest of the three
        st=[]
        while True:
            if node:
                if node.right:
                    st.append(node.right)
                st.append(node)
                node=node.right
            else:
                if st:
                    node=st.pop()
                    # Odd case, exchange curr and top element, when does this happen?
                    if st and node.right == st[-1]:
                        st.pop()
                        st.append(node)
                        node=node.right
                    else:
                        print(node.val, end=",")
                        node=None #Move to right or None
                else:
                    break

    def printLevelOrder(self, root): #BFS
        from collections import deque
        if not root:
            return []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                print(n.val if n else None, end=",")
                if n:
                    q.append(n.left)
                #if n.right:
                    q.append(n.right)

    def insertLevelOrder(self, arr, i=0, parent=None):
        n=len(arr)
        root=None
        # Base case for recursion
        if i < n and arr[i] is not None:
            root = Node(arr[i])
            root.parent=parent

            # insert left child
            root.left = self.insertLevelOrder(arr, 2 * i + 1, root)

            # insert right child
            root.right = self.insertLevelOrder(arr, 2 * i + 2, root)
        return root

# tree=Tree()
# root=tree.insertLevelOrder([1, 2, 3, 4, 5, 6, 6, 6, 6, 6])
# tree.inorder(root)




