"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# runtime: 63ms
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        
        return max_depth + 1

# runtime: 59ms      
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 1))
        depth = 0

        while queue:
            cur, val = queue.popleft()
            depth = val
            if cur.children:
                for child in cur.children:
                    queue.append((child, val + 1))
        return depth      
