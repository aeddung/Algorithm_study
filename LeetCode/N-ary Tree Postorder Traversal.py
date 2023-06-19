"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        visited = []
        for child in root.children:
            visited += self.postorder(child)
        
        visited += [root.val]
        return visited
