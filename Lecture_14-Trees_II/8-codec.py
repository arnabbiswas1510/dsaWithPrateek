"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""

class Codec:

    def serialize(self, root):
        if not root:
            return None

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"


    def deserialize(self, data):
        if not data:
            return None

        return self.deserialize_list(data)


    def deserialize_list(self, nums):
        from treeOperations import Node
        val = nums and nums.pop(0)
        if not val:
            return None

        root = Node(val)
        root.left = self.deserialize_list(nums)
        root.right = self.deserialize_list(nums)
        return root

c=Codec()
r=c.deserialize([1,2,3,None,None,4,5])
print(c.serialize(r))