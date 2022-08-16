"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""
import collections

def maxLevelSum(root) -> int:
    q = collections.deque()
    q.append(root)

    levelVals = {}
    currLevel = 1

    while q:
        for i in range(len(q)):
            node = q.popleft()

            if node:
                if str(currLevel) not in levelVals:
                    levelVals.update({str(currLevel): [node.val]})
                else:
                    levelVals[str(currLevel)].append(node.val)
                q.append(node.left if node.left else 0)
                q.append(node.right if node.right else 0)

        currLevel += 1

    result = max(levelVals, key = lambda i: sum(levelVals[i]))

    return result

from treeOperations import Tree

t=Tree()
r=t.insertLevelOrder([1,7,0,7,-8,None,None])
print(maxLevelSum(r))