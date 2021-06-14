"""
https://eugenejw.github.io/2017/07/leetcode-582

Simple and standard example that illustrates the technique of DFS and BFS
Connect by clause in Oracle for hierarchical queries follows DFS approach
"""

from collections import defaultdict
from collections import deque

def killProcessDFS(pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    def killAll(pid, children, killed):
        killed.append(pid)
        for child in children[pid]:
            killAll(child, children, killed)

    result = []
    children = defaultdict(set)
    for i in range(len(pid)):
        children[ppid[i]].add(pid[i])
    killAll(kill, children, result)
    return result

print(killProcessDFS([1, 3, 10, 5], [3, 0, 5, 3], 5))


def killProcessBFS(pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    result = []
    children = defaultdict(set)
    for i in range(len(pid)):
        children[ppid[i]].add(pid[i])
    q = deque()
    q.append(kill)
    while q:
        p = q.popleft()
        result.append(p)
        for child in children[p]:
            q.append(child)
    return result

print(killProcessBFS([1, 3, 10, 5], [3, 0, 5, 3], 5))