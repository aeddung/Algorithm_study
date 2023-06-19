"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        visited = []
        self.dfs(root, visited)
        return visited
    
    def dfs(self, root: 'Node', visited):
        if not root:
            return
        
        visited.append(root.val)
        for child in root.children:
            self.dfs(child, visited)

# 주어진 함수 그대로 사용            
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        visited = []
        if not root:
            return
        
        visited += [root.val]
        for child in root.children:
            visited += self.preorder(child)
        
        return visited            
